FROM python:3.10

RUN mkdir /fastapi

WORKDIR /fastapi

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

