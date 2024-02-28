# This is a Dockerfile for building a container image for the Aiden application.

# Use the official Python 3.8 slim image as the base image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the Aiden application directory from the local machine to the container
COPY aiden /app/aiden

# Copy the requirements.txt file from the local machine to the container
COPY requirements.txt /app

# Install the required Python packages
RUN pip install -r requirements.txt

# Set the default command to run when the container starts
CMD ["python", "-c", "import aiden; aiden_instance = aiden.Aiden()"]
