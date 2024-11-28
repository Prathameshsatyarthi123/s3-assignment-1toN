FROM python:3.11-alpine AS stageone

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:3.11-alpine

WORKDIR /app

COPY --from=stageone /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

COPY --from=stageone /app .

EXPOSE 8000

CMD ["python3", "app.py"]