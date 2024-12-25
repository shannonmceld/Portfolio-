import smtplib
from email.mime.text import MIMEText



# The email function
def test_email():
    try:
        sender = "emailgarrett93@gmail.com"
        recipient = "test_recipient@example.com"   
        subject = "Test Reminder"
        body = "This is a test reminder email."
        
         # Create email content
        message = MIMEText(body)
        message["From"] = sender
        message["To"] = recipient
        message["Subject"] = subject
        
        # Connect to SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            # Secure Connection
            server.starttls() 
            # Login
            server.login(sender,"jfcq umdk sibe hspx")
            server.sendmail(sender, recipient, message.as_string())
        print(f"Reminder email sent successfully to: {recipient}")
    
    except Exception as e:
        print(f"Failed to send reminder for task: {e}")
test_email()