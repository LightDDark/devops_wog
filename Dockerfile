FROM python:alpine

WORKDIR /app

COPY . .

RUN echo "4" > Scores.txt

RUN pip install -r req.txt

CMD ["python", "-m", "tests.e2e"]