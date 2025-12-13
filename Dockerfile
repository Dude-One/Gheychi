FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port
EXPOSE 8080

# Use uvicorn for FastAPI
CMD ["uvicorn", "Main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
