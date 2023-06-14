
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession,
                                    create_async_engine)
from sqlalchemy.orm import declarative_base, sessionmaker

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = (f"postgresql+asyncpg://"
                f"{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

Base = declarative_base()
metadata = MetaData()
engine = create_async_engine(url=DATABASE_URL, echo=False)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

def create_all(engine: AsyncEngine) -> None:
    return metadata.create_all(engine)

async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session