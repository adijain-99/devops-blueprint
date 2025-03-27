# Use official Python runtime as base image
FROM python:3.9-slim-buster

# Set working directory in the container
WORKDIR /app

# Copy only requirements file first to leverage Docker cache
COPY requirements.txt .

# Install system dependencies and Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Use environment variable for port (optional)
ENV PORT=5000

# Use gunicorn as production WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "app:app"]
