import requests
from mimesis import Person
from mimesis.locales import Locale

fake = Person(Locale.EN)
email = fake.email(domains=['gmail.com'])
print(email)
count = 0

def test_create_query():
    response = requests.post(
        url="http://localhost:8000/early-access/",
        json={
            "email": email,
            "type": "main",
        },
    )
    print(response.json())
    assert response.status_code == 201
    assert response.json()["id"] == count
    assert response.json()["email"] == email
    assert response.json()["type"] == "main"
    assert response.json()["status"] == "waiting"

def test_create_query_again():
    response = requests.post(
        url="http://localhost:8000/early-access/",
        json={
            "email": email,
            "type": "main",
        },
    )
    assert response.json()["status_code"] == 409
    assert response.json()["detail"] == "query already exists"

def test_get_queries():
    response = requests.get(
        url="http://localhost:8000/early-access/",
        headers={"limit": "10"}
    )
    assert response.status_code == 200
    assert response.json()["count"] == 1
    assert response.json()["items"][0]["id"] == count
    assert response.json()["items"][0]["email"] == email
    assert response.json()["items"][0]["type"] == "main"
    assert response.json()["items"][0]["status"] == "waiting"
