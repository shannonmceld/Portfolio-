import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
import logging
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from flask import url_for


mail = Mail()

load_dotenv()

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s", 
    handlers=[
        logging.FileHandler("email_errors.log"), # Logs to a file 
        logging.StreamHandler() # Logs to console 
        ] 
    )

sender_email = os.getenv('EMAIL_USER')
password = os.getenv("EMAIL_PASS")

def generate_reset_token(email, secret_key, expiation=3600):
    serializer = URLSafeTimedSerializer(secret_key)
    return serializer.dumps(email, salt='password-reset-salt')


def validate_reset_token(token, secret_key, expiration=3600):
    serializer = URLSafeTimedSerializer(secret_key)
    try:
        email = serializer.loads(token, salt ='password-reset-salt', max_age ='experation')
        return email
    except:
        return None
    
    
def send_reset_email(user_email, app):
    token = generate_reset_token(user_email, app.configure['SECRET_KEY'])
    reset_url = url_for('reset_password', token=token, _external=True)
    msg = Message('Password Reset Request',
                  sender = sender_email,
                  recipients=[user_email])
    msg.body = f"Click the link to reset your password:{reset_url}"
    mail.send(msg)
                                                                                  
# The email function
def send_email(task):
    try:
        to_email = task.email
        
        subject = f"reminder for Task: {task.title}" 
        body = f"""
        Hi, 
        
        This is a reminder for your task:{task.title}.
        Due Date: {task.due_date.strftime('%Y-%m-%d %H:%M')}.
        Description: {task.description or 'No Description Provided.'}
        
        Regards,
        Task Reminder App
        """
    
    
        # Create email content
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, 'plain'))
        
        # Connect to SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            # Secure Connection
            server.starttls() 
            # Login
            server.login(sender_email, password) 
            # Send Email
            server.sendmail(sender_email, to_email, message.as_string())
        try:
            logging.info(f"Attempting to send email to {to_email}") # Connect to SMTP server and send email... 
            logging.info(f"Reminder email sent successfully to: {to_email}") 
        except Exception as e:
            logging.error(f"Failed to send reminder for task {task.title}: {e}")
    
    except Exception as e:
        logging.error(f"Failed to send reminder for task {task.title}: {e}")
        print(f"Failed to send reminder for task {task.title}: {e}")





    