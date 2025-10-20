FROM python:3.9.4
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.fastapi_part:app", "--host", "0.0.0.0", "--port", "8000"]
