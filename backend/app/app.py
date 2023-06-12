from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_limiter import FastAPILimiter
from redis import asyncio as aioredis

from config import REDIS_HOST, REDIS_PORT
from db import Base, engine
from early_access.routers import router as early_access_router

# from lobby.routers import router as lobby_router
# from reply.routers import router as reply_router
# from report.routers import router as report_router
# from message.routers import router as message_router

app = FastAPI(
    title='Thoughty',
    version='1.0',
)

app.include_router(
    router=early_access_router,
)
# app.include_router(
#     lobby_router,
# )
# app.include_router(
#     reply_router,
# )
# app.include_router(
#     report_router,
# )
# app.include_router(
#     message_router,
# )


origins = [
    'http://localhost:8000',
    'http://localhost:1111',
    'http://frontend:8000',
    'http://webserver:8000',
    'http://webserver:80',
    'http://localhost',
    'http://webserver',
    'http://frontend',
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=[
        "POST",
        "PATCH",
    ],
    allow_headers=[
        'Content-Type',
        'Set-Cookie',
        'Access-Control-Allow-Headers',
        'Access-Control-Allow-Origin',
        'Authorization',
        'Accept-Language',
    ],
)
#app.add_middleware(HTTPSRedirectMiddleware)


@app.on_event('startup')
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    redis = aioredis.from_url(f'redis://{REDIS_HOST}:{REDIS_PORT}', encoding='utf8', decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
    await FastAPILimiter.init(redis)
