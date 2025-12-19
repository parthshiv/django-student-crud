FROM python:3.11.9-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements.txt from root and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory (excluding virtualenv etc)
COPY . .

# Expose port for Django
EXPOSE 8000

# Run Django development server
CMD ["python", "crud/manage.py", "runserver", "0.0.0.0:8000"]
