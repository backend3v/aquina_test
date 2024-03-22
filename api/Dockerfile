
FROM python:3.9-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./ ./api
WORKDIR /api
EXPOSE 8080
CMD ["uvicorn", "launcher_api:server", "--host", "0.0.0.0", "--port", "8080"]