FROM python:3.9

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt --no-cache-dir

ENV PYTHONUNBUFFERED=1

COPY producer.py .

CMD [ "python", "producer.py" ]
