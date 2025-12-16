# Django Student CRUD

![Django](https://img.shields.io/badge/Django-4.x-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## Description
**Django Student CRUD** is a simple Django-based application for managing student records.  
It supports full CRUD operations:

- **C**reate – Add new students  
- **R**ead – View student details and list  
- **U**pdate – Edit existing student information  
- **D**elete – Remove student records  

This project is ideal for learning Django models, forms, and views while building a functional student management system.

## Features
- Add new students with name, email, and password  
- Update student information  
- Delete student records  
- View all students in a dashboard  

## Technologies Used
- Python 3.x  
- Django 4.x  
- SQLite (default database)  

## Installation & Setup
1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/django-student-crud.git
cd django-student-crud
```

## Install dependencies:
```bash
pip install -r requirements.txt
```

## Apply migrations:
```bash
python manage.py migrate
```

## Run the development server:
```bash
python manage.py runserver
```

## Access the app:
Open your browser and go to http://127.0.0.1:8000/

## Usage

Navigate to /add_student to add a new student

Navigate to /edit_student/<id> to update student details

Navigate to /delete_student/<id> to delete a student

Navigate to /dashboard to view all students

## Testing

This project includes unit tests for CRUD operations at the model level. To run tests:
```bash
python manage.py test enroll
```
