FROM python:alpine

WORKDIR /app

COPY ./front .
COPY ./utils .

CMD ["python", "-m", "front.main_score"]