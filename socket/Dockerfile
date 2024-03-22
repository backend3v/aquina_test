FROM python:3.9-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./ ./socket
WORKDIR /socket
EXPOSE 8765
CMD ["python","launcher_socket.py"]