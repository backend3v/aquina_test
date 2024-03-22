# Use the official Python base image
FROM python:3.9-slim
# Set the working directory inside the container

# Copy the requirements file to the working directory
COPY requirements.txt .
# Install the Python dependencies
RUN pip install -r requirements.txt
# Copy the application code to the working directory
COPY ./ ./socket
# Expose the port on which the application will run
WORKDIR /socket
EXPOSE 8765

# Run the FastAPI application using uvicorn server
CMD ["python","launcher_socket.py"]