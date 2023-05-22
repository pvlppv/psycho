import json
from math import ceil
from typing import List
from fastapi import APIRouter, HTTPException, Depends, Path, Request, Response, WebSocket, WebSocketDisconnect, status
from fastapi.responses import HTMLResponse
from fastapi_cache import FastAPICache
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from db import get_async_session
from reply.models import Reply
from reply.schemas import Reply_Read, Reply_EN_Create, Reply_RU_Create
from fastapi_cache.decorator import cache
from db import async_session_maker
from fastapi_limiter.depends import RateLimiter, WebSocketRateLimiter
from uuid import UUID
import asyncio


router = APIRouter(
    tags=['reply']
)


async def default_callback(request: Request, response: Response, pexpire: int):
    await asyncio.sleep(2)
    

@router.post(
    '/reply/get', 
    responses={
        status.HTTP_200_OK: {
            'model': List[Reply_Read], 
            'description': 'Successful Response',
        },  
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            'description': 'Internal Server Error',
        },
    }, 
    # dependencies=[Depends(RateLimiter(times=2, seconds=5, callback=default_callback))],
)
async def reply_get(
    page: int = 1, limit: int = 10, 
    session: AsyncSession = Depends(get_async_session),
):
    try:
        offset = (page - 1) * limit
        query = select(Reply).order_by(Reply.id.desc()).offset(offset).limit(limit)
        result = await session.execute(query)
        data = result.scalars().all()
        return [Reply_Read.from_orm(item) for item in data]
    except Exception:
        raise HTTPException(status_code=500)


@router.post(
    '/en/reply/post', 
    responses={
        status.HTTP_200_OK: {
            'model': List[Reply_Read], 
            'description': 'Successful Response',
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            'description': 'Internal Server Error',
        },
    }, 
    # dependencies=[Depends(RateLimiter(times=1, seconds=30, callback=default_callback))],
)
async def reply_EN_post(
    reply_create: Reply_EN_Create, 
    session: AsyncSession = Depends(get_async_session)
):
    stmt = insert(Reply).values(**reply_create.dict())
    await session.execute(stmt)
    await session.commit()
    return reply_create


@router.post(
    '/ru/reply/post', 
    responses={
        status.HTTP_200_OK: {
            'model': List[Reply_Read], 
            'description': 'Successful Response',
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            'description': 'Internal Server Error',
        },
    }, 
    # dependencies=[Depends(RateLimiter(times=1, seconds=30, callback=default_callback))],
)
async def reply_RU_post(
    reply_create: Reply_RU_Create, 
    session: AsyncSession = Depends(get_async_session)
):
    stmt = insert(Reply).values(**reply_create.dict())
    await session.execute(stmt)
    await session.commit()
    return reply_create
