import smtplib
from email.mime.text import MIMEText
import logging


# The email function
def send_email(subject, body, to_email):
    try:
        print(f"Sending Email...{to_email} with subject: {subject} and body: {body}")
        logging.info(f"Sending Email...{to_email} with subject: {subject} and body: {body}")
        sender_email = "emailgarrett93@gmail.com"
        password = "jfcq umdk sibe hspx"
    except smtplib.SMTPConnectError as e:
        logging.error(f"Network issue: Unable to cnonnectto SMTP server: {e}")
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")
        raise
    

    # Create email content
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email
    
    try:
        # Connect to SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            # Secure Connection
            server.starttls() 
            # Login
            server.login(sender_email, password) 
            # Send Email
            server.sendmail(sender_email, to_email, msg.as_string()) 
        logging.info(f"Email Sent Successfully!")
        print("Email Sent Successfully")
    except Exception as e:
        logging.error(f"Error: {e}")
        print(f"Error: {e}")
    
# schedule.every(1).second.do(lambda: send_email("Test subject", "Test Body", "shannonmceld@gmail.com"))
    