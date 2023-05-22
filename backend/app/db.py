from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

# database connection
DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# database accumulation 
Base = declarative_base()

# engine
engine = create_async_engine(DATABASE_URL, poolclass=NullPool)

# session
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# управлять жизненным циклом асинхронной сессии базы данных
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

