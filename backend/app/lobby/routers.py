import asyncio
import json
from typing import List

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Path,
    Request,
    Response,
    WebSocket,
    WebSocketDisconnect,
    status,
)
from fastapi_limiter.depends import WebSocketRateLimiter
from pydantic import ValidationError
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from db import async_session_maker, get_async_session
from lobby.models import Message
from lobby.schemas import Lobby_Read, Message_EN_Create, Message_RU_Create

router = APIRouter(tags=["lobby"])


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(
        self, message: str, websocket: WebSocket, locale: str = Path(regex="^(en|ru)$")
    ):
        try:
            message_dict = json.loads(message)
            if locale == "ru":
                lobby_message = Message_RU_Create(**message_dict["data"])
                await self.message_RU_create(lobby_message)
            else:
                lobby_message = Message_EN_Create(**message_dict["data"])
                await self.message_EN_create(lobby_message)
            for connection in self.active_connections:
                await connection.send_json(message_dict)
        except ValidationError as e:
            error_message = e.errors()[0]["msg"]
            await websocket.send_json({"event": "error", "data": error_message})

    @staticmethod
    async def message_EN_create(message: Message_EN_Create):
        async with async_session_maker() as session:
            stmt = insert(Message).values(**message.dict())
            await session.execute(stmt)
            await session.commit()

    @staticmethod
    async def message_RU_create(message: Message_RU_Create):
        async with async_session_maker() as session:
            stmt = insert(Message).values(**message.dict())
            await session.execute(stmt)
            await session.commit()


manager = ConnectionManager()


@router.websocket("/{locale}/ws")
async def websocket_endpoint(
    websocket: WebSocket, locale: str = Path(regex="^(en|ru)$")
):
    await manager.connect(websocket)
    ratelimit = WebSocketRateLimiter(times=1, seconds=30)
    try:
        while True:
            try:
                message = await websocket.receive_text()
                await ratelimit(websocket)
                message_dict = {
                    "event": "success",
                    "data": {"message_text": message, "lobby_name": locale},
                }
                message_json = json.dumps(message_dict)
                await manager.broadcast(message_json, websocket, locale)
            except HTTPException:
                await websocket.send_json(
                    {
                        "event": "error",
                        "data": "Сообщения можно отправлять раз в 30 секунд.",
                    }
                )
    except WebSocketDisconnect:
        manager.disconnect(websocket)


async def default_callback(request: Request, response: Response, pexpire: int):
    await asyncio.sleep(2)


@router.get(
    "/{locale}/lobby/get",
    responses={
        status.HTTP_200_OK: {
            "model": List[Lobby_Read],
            "description": "Successful Response",
        },
        status.HTTP_429_TOO_MANY_REQUESTS: {
            "description": "Too Many Requests",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Internal Server Error",
        },
    },
    # dependencies=[Depends(RateLimiter(times=2, seconds=5, callback=default_callback))],
)
async def lobby_get(
    locale: str = Path(regex="^(en|ru)$"),
    limit: int = 10,
    skip: int = 0,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        offset = skip
        query = (
            select(Message)
            .where(Message.lobby_name == locale)
            .order_by(Message.id.desc())
            .offset(offset)
            .limit(limit)
        )
        result = await session.execute(query)
        data = result.scalars().all()
        return [Lobby_Read.from_orm(item) for item in data]
    except Exception:
        raise HTTPException(status_code=500, detail=Exception)
