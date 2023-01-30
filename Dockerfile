FROM python:3.9.15

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python AccordPret/manage.py runserver