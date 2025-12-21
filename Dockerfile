FROM parthshivu/django-student-crud

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Application code
COPY . /app

# Create the folder for the database
RUN mkdir -p /app/crud/db_folder

# Give permissions so Django can write to the database file
RUN chmod -R 777 /app/crud/db_folder

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
