import typing

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from early_access import models
from early_access.schemas import (GetResponse, PatchRequest, PatchResponse,
                                  PostRequest, PostResponse)


class EarlyAccess:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
    
    async def create(self, query: PostRequest) -> PostResponse:
        database_query = models.EarlyAccess(**query.dict())
        self.session.add(database_query)
        await self.session.flush()
        await self.session.refresh(database_query)
        await self.session.commit()
        return database_query

    async def get(self, limit: typing.Optional[int] = 15) -> GetResponse:
        query = select(models.EarlyAccess).limit(limit)
        result = await self.session.execute(query)
        response = result.scalars().all()
        return len(response), response

    async def get_by_id(self, id: int) -> PostResponse:
        query = select(models.EarlyAccess).where(models.EarlyAccess.id==id)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def edit_status(self, query: PatchRequest) -> PatchResponse:
        return

    async def email_exist(self, email: str) -> bool:
        query = select(models.EarlyAccess).where(models.EarlyAccess.email==email)
        result = await self.session.execute(query)
        if len(result.scalars().all()) >= 1:
            return True
        return False
