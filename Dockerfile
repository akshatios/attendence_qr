# # Base image
# FROM python:3.10-slim

# # Set working directory
# WORKDIR /app

# # Copy all project files
# COPY . /app

# # Install dependencies
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# # Collect static files (optional)
# RUN python manage.py collectstatic --noinput || true

# # Expose port
# EXPOSE 8000

# # Start the app
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run migrations & collect static (optional, for production)
# CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
