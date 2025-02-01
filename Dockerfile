# Use official Python image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app


# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose port 8000
EXPOSE 8000

# Run migrations and start server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "moviebackend.wsgi:application"]
