from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

from config import REDIS_HOST, REDIS_PORT
from lobby.routers import router as lobby_router
from reply.routers import router as reply_router
from report.routers import router as report_router
from message.routers import router as message_router

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

from fastapi_limiter import FastAPILimiter


app = FastAPI(
    title='Thoughty',
    version='1.0',
)


app.include_router(
    lobby_router,
)
app.include_router(
    reply_router,
)
app.include_router(
    report_router,
)
app.include_router(
    message_router,
)


origins = [
    'http://localhost:5173',
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=['Content-Type', 'Set-Cookie', 'Access-Control-Allow-Headers', 'Access-Control-Allow-Origin',
                   'Authorization', 'Accept-Language'],
)
# app.add_middleware(HTTPSRedirectMiddleware)
# app.middleware('http')(locale)


@app.on_event('startup')
async def startup_event():
    redis = aioredis.from_url(f'redis://{REDIS_HOST}:{REDIS_PORT}', encoding='utf8', decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
    await FastAPILimiter.init(redis)
