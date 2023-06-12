import typing

from fastapi import APIRouter, Depends, HTTPException, Path, responses, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_async_session
from early_access import crud
from early_access.schemas import (GetResponse, PatchRequest, PatchResponse,
                                  PostRequest, PostResponse)

router = APIRouter(
    prefix="/early-access",
    tags=["/early-access"],
)

@router.get(
    path="/",
    response_model=GetResponse,
    status_code=status.HTTP_200_OK,
    description="GET request to get all queries",
    response_description="if successful, we get 200 code and response model",
)
async def get_query(
        limit: typing.Optional[int] = 15,
        session: AsyncSession = Depends(get_async_session),
) -> responses.JSONResponse:
    session_crud = crud.EarlyAccess(session)
    len, queries = await session_crud.get(limit)
    return {
        "count": len,
        "items": queries,
    }


@router.get(
    path="/{id}",
    response_model=PostResponse,
    status_code=status.HTTP_200_OK,
    description="GET request to get one by id query",
    response_description="if successful, we get 200 code and response model",
)
async def get_query_by_id(
        id: int = Path(example=1),
        session: AsyncSession = Depends(get_async_session),
) -> responses.JSONResponse:
    session_crud = crud.EarlyAccess(session)
    result = await session_crud.get_by_id(id)
    if not result:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="query not found",
            headers=None,
        )
    return {
        "id": result.id,
        "email": result.email,
        "type": result.type,
        "status": result.status,
        "created_at": result.created_at,
    }


@router.post(
    path="/",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
    description="POST request to create query",
    response_description="if successful, we get 201 code and response model",
    responses={
        status.HTTP_201_CREATED: {
            "model": PostResponse,
        },
        status.HTTP_409_CONFLICT: {
            "description": "if email is in the database, "
                           "we get 401 code and error description",
            "content": {
                "application/json": {
                    "example": {"detail": "query already exists"}
                }
            },
        },
    },
)
async def create_query(
        query: PostRequest,
        session: AsyncSession = Depends(get_async_session),
) -> responses.JSONResponse:
    session_crud = crud.EarlyAccess(session)
    if await session_crud.email_exist(query.email):
        return HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="query already exists",
        )
    result = await session_crud.create(query)
    return {
        "id": result.id,
        "email": result.email,
        "type": result.type,
        "status": result.status,
        "created_at": result.created_at,
    }


@router.patch(
    path="/",
    response_model=PatchResponse,
    status_code=status.HTTP_200_OK,
    description="PATCH request to change query status",
    response_description="if successful, we get 200 code and new status",
)
async def edit_status(
        request: PatchRequest,
        session: AsyncSession = Depends(get_async_session),
) -> responses.JSONResponse:
    return {
        "test": "ok"
    }