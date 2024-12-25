# Task Scheduling Application

This is a robust and user-friendly task scheduling application built with Flask, SQLAlchemy, and Python. The app allows users to create, view, update, and delete tasks while incorporating email reminders for due tasks. Designed with security and scalability in mind, it offers essential features for effective time management.

## Features

User Authentication: Secure registration and login using hashed passwords.
Task Management: CRUD operations for tasks, including titles, descriptions, due dates, and completion status.
Email Reminders: Automated email reminders for tasks nearing their due dates.
Scheduler Integration: Uses Flask-APScheduler to send reminders on time.
Responsive UI: Clean and easy-to-navigate interface for users.
Installation
Clone this repository:

cd task-scheduler

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
flask db upgrade

Set SECRET_KEY and database URIs for production in a .env file.
Run the application:

flask run
n

### Usage

Register and log in to access the dashboard.
Create tasks with specific due dates and email reminders.
Update or delete tasks as needed.
View pending tasks and receive email reminders for due tasks.

### Project Structure

task-scheduler/
│
├── app.py                # Main application file
├── models.py             # Database models for users and tasks
├── forms.py              # Forms for user input
├── templates/            # HTML templates
├── static/               # CSS and JS files
├── send_email.py         # Email sending logic
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

### Contact

This project was created by Shannon McElderry.
Feel free to reach out with feedback or sugestions!
