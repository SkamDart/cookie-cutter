FROM python:3.7-alpine

COPY requirements.txt /

RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["gunicorn", "-w 4", "wsgi:app"]
