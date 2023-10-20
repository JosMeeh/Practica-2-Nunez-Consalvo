# Use the official Python image as the base image
FROM python:3.11-slim-buster

# Copy the files into the container
COPY . /app

# Set the working directory in the container
WORKDIR /app

# Install FastAPI, Uvicorn, Alembic, and PostgreSQL client
RUN pip install fastapi uvicorn alembic psycopg2-binary

# Expose the port that FastAPI will run on
EXPOSE 8000

# Set the entry point to your entrypoint.sh script
ENTRYPOINT ["app/entrypoint.sh"]
