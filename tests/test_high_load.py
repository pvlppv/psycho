import aiohttp
import pytest
from mimesis import Person
from mimesis.locales import Locale

fake = Person(Locale.EN)
domains = [
    "gmail.com",
    "outlook.com",
    "yahoo.com",
    "yandex.ru",
    "aol.com",
    "mail.com",
    "zoho.com",
    "protonmail.com",
    "icloud.com",
    "gmx.com",
    "hotmail.com",
    "mail.ru",
    "live.com",
    "qq.com",
    "163.com",
    "sina.com.cn",
    "rediffmail.com",
    "indiatimes.com",
    "mailinator.com",
    "gmial.com",
    "tutanota.com",
    "fastmail.com",
    "hushmail.com",
    "lavabit.com",
    "rambler.ru",
    "seznam.cz",
    "libero.it",
    "web.de",
    "t-online.de",
    "gmx.de",
    "ymail.com",
    "hotmail.co.uk",
    "mail.co.uk",
    "orange.fr",
    "laposte.net",
    "yandex.com",
    "aol.co.uk",
    "zoho.eu",
    "protonmail.ch",
    "icloud.co.uk",
    "fastmail.fm",
    "mail.comcast.net",
    "centurylink.net",
    "mail.bellsouth.net",
    "cox.net",
    "charter.net",
    "att.net",
    "verizon.net",
    "hotmail.fr",
    "mail.bg",
    "tut.by",
    "mail.ee",
    "mail.kz",
    "mail.ua",
    "poczta.fm",
    "wp.pl",
    "onet.pl",
    "interia.pl",
    "o2.pl",
    "seznam.sk",
    "mail.be",
    "tiscali.it",
    "libero.it",
    "hotmail.de",
    "ymail.com.au",
    "gmx.at",
    "mail.com.br",
    "mail.ch",
    "protonmail.de",
    "icloud.com.au",
    "mail.com.mx",
    "mail.co.za",
    "hotmail.com.ar",
    "mail.pt",
    "mail.ro",
    "ymail.com.sg",
    "gmx.es",
    "yandex.kz",
    "mail.ru",
    "inbox.lv",
    "mail.mn",
    "mail.gr",
    "hotmail.it",
    "ymail.com.ph",
    "yahoo.com.br",
    "yahoo.com.mx",
    "yahoo.co.jp",
    "ymail.com.my",
    "mail.com.co",
    "yahoo.com.au",
]
backend_url = "http://localhost:8000/early-access/"


async def aiohttp_post(url: str, json_data: dict):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=json_data) as response:
            return response.status, await response.json()

@pytest.mark.benchmark
async def test_highload(count: int = 10000) -> None:
    for _ in range(count):
        email = fake.email(domains)
        status, json = await aiohttp_post(
            url="http://localhost:8000/early-access/",
            json_data={
                "email": email,
                "type": "main",
            },
        )
        assert status == 201
        assert json["email"] == email
