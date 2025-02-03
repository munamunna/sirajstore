# Use official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Set the environment variable
ENV DJANGO_SETTINGS_MODULE=moviebackend.settings



# Expose the application port
EXPOSE 8000

# Command to start the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "moviebackend.wsgi:application"]
