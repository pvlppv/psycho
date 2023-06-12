import asyncio
import json
from math import ceil
from typing import List
from uuid import UUID

from fastapi import (APIRouter, Depends, HTTPException, Path, Request,
                     Response, WebSocket, WebSocketDisconnect, status)
from fastapi.responses import HTMLResponse
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache
from fastapi_limiter.depends import RateLimiter, WebSocketRateLimiter
from pydantic import ValidationError
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from db import async_session_maker, get_async_session
from report.models import Report
from report.schemas import Report_Create, Report_Read

router = APIRouter(
    tags=['report']
)


async def default_callback(request: Request, response: Response, pexpire: int):
    await asyncio.sleep(2)
    

@router.post(
    '/report/get', 
    responses={
        status.HTTP_200_OK: {
            'model': List[Report_Read], 
            'description': 'Successful Response',
        },  
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            'description': 'Internal Server Error',
        },
    }, 
    # dependencies=[Depends(RateLimiter(times=2, seconds=5, callback=default_callback))],
)
async def report_get(
    page: int = 1, limit: int = 10, 
    session: AsyncSession = Depends(get_async_session),
):
    try:
        offset = (page - 1) * limit
        query = select(Report).order_by(Report.id.desc()).offset(offset).limit(limit)
        result = await session.execute(query)
        data = result.scalars().all()
        return [Report_Read.from_orm(item) for item in data]
    except Exception:
        raise HTTPException(status_code=500)


@router.post(
    '/report/post', 
    responses={
        status.HTTP_200_OK: {
            'model': List[Report_Read], 
            'description': 'Successful Response',
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            'description': 'Internal Server Error',
        },
    }, 
    # dependencies=[Depends(RateLimiter(times=2, seconds=5, callback=default_callback))],
)
async def report_post(report_create: Report_Create, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Report).values(**report_create.dict())
    await session.execute(stmt)
    await session.commit()
    return report_create
