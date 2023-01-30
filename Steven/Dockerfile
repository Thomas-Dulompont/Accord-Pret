# app/Dockerfile

FROM python:3.9.15

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD  uvicorn api:app --host 0.0.0.0