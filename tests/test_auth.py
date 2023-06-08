from httpx import AsyncClient


async def test_lobby_en(ac: AsyncClient):
    response = await ac.post("/register", json={
        "email": "paulpopov78@gmail.com",
        "password": "12345678",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": 12345678,
        "created_at": "2023-04-14T06:58:32.652"
    })

    assert response.status_code == 201


async def test_lobby_ru(ac: AsyncClient):
    response = await ac.post("/register", json={
        "email": "paulpopov78@gmail.com",
        "password": "12345678",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": 12345678,
        "created_at": "2023-04-14T06:58:32.652"
    })

    assert response.status_code == 201
