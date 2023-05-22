<h1>Thoughty App</h1>

бэкенд:
FastAPI

база данных:
PostgreSQL - sqlalchemy, alembic, asyncpg

аутентификация:
custom, fastapi-users[sql-alchemy]

админка:
fastapi-admin

веб-сокеты:
fastapi-websockets 

кеширование:
redis, fastapi-cache2[redis]

фоновые задачи:
fastapi-BackgroundTasks, Celery

тесты:
pytest, pytest-asyncio

фронтенд:
Vue.js

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

pip:
- pip install fastapi[all]
- pip install sqlalchemy alembic asyncpg
- pip install pytest pytest-asyncio
- pip install fastapi-cache2[redis]
- pip install fastapi-limiter
- pip install pymorphy2
- pip insta pytz

migrations:
- alembic init migrations
- alembic revision —autogenerate -m 'title'
- alembic upgrade head
- alembic downgrade ‘revision title’

git:
- git status
- git log
- git add .
- git commit -m ‘comment’
- git push

tests:
- pytest -v -s tests

redis:
- redis-cli



