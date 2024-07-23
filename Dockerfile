FROM python:alpine

WORKDIR /app

COPY front ./front
COPY utils ./utils

RUN pip install --no-cache-dir Flask

CMD ["python", "-m", "front.main_score"]
