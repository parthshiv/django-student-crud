FROM python:3.11.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential zip libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Run tests (optional: can remove in production image)
RUN mkdir -p reports
RUN python manage.py test --verbosity=2 --testrunner=xmlrunner.extra.djangotestrunner.XMLTestRunner --output=reports || true

# Expose port
EXPOSE 8000

# Apply migrations and run server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
