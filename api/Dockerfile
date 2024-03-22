# Use the official Python base image
FROM python:3.9-slim
# Set the working directory inside the container

# Copy the requirements file to the working directory
COPY requirements.txt .
# Install the Python dependencies
RUN pip install -r requirements.txt
# Copy the application code to the working directory
COPY ./ ./api
# Expose the port on which the application will run
WORKDIR /api
EXPOSE 8080

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "launcher_api:server", "--host", "0.0.0.0", "--port", "8080"]