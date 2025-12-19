# Stage 1: Build & test
FROM python:3.11.9-slim AS builder

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    zip \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Run Django tests and generate XML reports
RUN mkdir -p reports
RUN python manage.py test --verbosity=2 --testrunner=xmlrunner.extra.djangotestrunner.XMLTestRunner --output=reports || exit 1

# Stage 2: Final deployable image
FROM python:3.11.9-slim

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy venv from builder stage
COPY --from=builder /app/venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Copy app code
COPY --from=builder /app /app

# Expose port
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
