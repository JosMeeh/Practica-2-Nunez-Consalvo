# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the FastAPI app code into the container
COPY ./main.py /app/main.py

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to start the FastAPI app using Uvicorn and listen on all available network interfaces
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
