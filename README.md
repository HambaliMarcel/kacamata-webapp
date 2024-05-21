# Kacamata WebApp

Welcome to **Kacamata WebApp**, a simple yet powerful Django-based web application designed to upload, manage, and share educational materials for elementary school students from grades 1 to 6. This project aims to provide an easy-to-use platform for educators to organize and distribute learning resources effectively.

## Features

- **Upload Educational Materials**: Teachers can easily upload various educational materials such as PDFs, documents, and presentations.
- **Organize by Grade**: Materials are organized by grade levels (1-6) to ensure students and teachers can find the relevant resources quickly.
- **Secure Access**: Secure file handling and storage to keep educational materials safe.
- **User-Friendly Interface**: Intuitive and simple user interface for both educators and students.
- **Admin Management**: Full control over the content through the Django admin interface.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed
- Django 3.x or higher installed
- Git installed
- Virtual environment setup (optional but recommended)

### Installation

```bash
# Clone the Repository
git clone https://github.com/yourusername/kacamata-webapp.git
cd kacamata-webapp

# Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install Dependencies
pip install -r requirements.txt

# Apply Migrations
python manage.py makemigrations
python manage.py migrate

# Create a Superuser
python manage.py createsuperuser

```

### Run the Server
```bash
python manage.py runserver
```
### Access the Application
Open your web browser and go to http://127.0.0.1:8000 to access Kacamata WebApp.

### Usage
  - Uploading Materials
  Log in as an admin at http://127.0.0.1:8000/admin.
  Navigate to the "Materi" section.
  Add new material by providing a title, description, grade level, and upload the file.
  - Viewing Materials
  Go to the main page http://127.0.0.1:8000/.
  Browse materials organized by grade levels.
