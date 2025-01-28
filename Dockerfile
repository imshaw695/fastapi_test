# Use official Python 3.11 runtime as a parent image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY /back_end/requirements.txt requirements.txt

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY /back_end .

# Make port 8080 available to the world outside the container
# Cloud Run requires using the port defined by PORT environment variable
ENV PORT 8080

# Run the application
CMD ["uvicorn", "wsgi:app", "--host", "0.0.0.0", "--port", "8080"]