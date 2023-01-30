FROM python:3.9.15

copy . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python manage.py runserver