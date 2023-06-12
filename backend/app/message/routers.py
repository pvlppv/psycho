import asyncio
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_async_session
from lobby.models import Message
from message.schemas import Message_Read

router = APIRouter(
    tags=['message']
)

@router.get(
    '/messages/{message_id}', 
    responses={
        status.HTTP_200_OK: {
            'model': List[Message_Read], 
            'description': 'Successful Response',
        },  
        status.HTTP_429_TOO_MANY_REQUESTS: {
            'description': 'Too Many Requests',
        },  
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            'description': 'Internal Server Error',
        },
    }, 
)
async def message_get(
    message_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        query = select(Message).where(Message.id == message_id)
        result = await session.execute(query)
        data = result.scalars().all()
        return [Message_Read.from_orm(item) for item in data]
    except Exception:
        raise HTTPException(status_code=500)

