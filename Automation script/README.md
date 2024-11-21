#Email Automation with Python

##Overview
This is a Python-based email automation script designed for sending personalized emails using data from a CSV file. The program supports error handling, logging, and task scheduling, making it ideal for streamlining email workflows.



Key Features
• Reads recipient details (email, subject, body) from a CSV file.

• Validates input data and logs errors for missing or invalid fields.

• Handles network issues and logs connection errors gracefully.

• Includes fallback logging to console or temporary files when file permissions are restricted.

• Supports task scheduling for automated email sending at specified intervals.


##Setup Instructions

###Requirements
• Python 3.8+

• Required libraries:

• smtplib

• schedule

• logging

• csv

• sys

• tempfile


###Installation
1. Clone or download the repository.

2. Install necessary dependencies using:
    pip install -r requirements.txt

3. Configure your SMTP settings in the script.


##How to Use

1. Prepare Your CSV File

Create a CSV file named emails.csv with the following headers:

• recipient_email: The recipient’s email address.

• subject: The subject of the email.

• body: The body content of the email.

2. Configure SMTP Server

Update the script with your email provider’s SMTP server and port details, along with your credentials:
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "your-email@example.com"
password = "your-password"

3. Run the Script

To send emails:
python email_automation.py

4. Schedule Emails

Use the task scheduling feature to automate sending at intervals:
schedule.every(1).hours.do(send_email_task)
Error Handling
• Invalid email addresses, network failures, and missing fields are logged.

• If the log file is unwritable, logs are redirected to the console or a temporary file.

• Comprehensive error handling ensures the program continues running seamlessly.

##Logging

###The program generates detailed logs for:

• Email success or failure.

• Input validation errors.

• SMTP connection issues.

• Permissions errors with fallback logging mechanisms.

##Testing

###The program has been tested for:

• Missing fields in CSV.

• Invalid email formats.

• Simulated network failures.

• File and directory permission restrictions.

##Future Enhancements

• Add GUI support for non-technical users.

• Implement support for additional file formats (e.g., Excel).

• Enhance logging with email status dashboards.

Contact

This project was created by Shannon McElderry.
Feel free to reach out with feedback or sugestions!
