FROM python:3.10-slim
COPY . /fastapi/
WORKDIR /fastapi
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod a+x docker/*.sh