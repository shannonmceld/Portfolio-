import schedule
import time
import csv
from email_utils import send_email 
import re
import logging
import sys


try:
    logging.basicConfig(
        #log filename
        filename='email_log.log',
        # Log level (INFO for general tracking)
        level=logging.INFO,
        # log format
        format="%(asctime)s - %(levelname)s - %(message)s")
    logging.info("Logging initialized successfully.")
except (PermissionError, IOError) as e:
    print(f"Logging to file failed: {e}")
    logging.basicConfig(
        stream=sys.stdout,
        # Log level (Error for when file is not writable)
        level=logging.ERROR,
        # log format
        format="%(asctime)s - %(levelname)s - %(message)s")
    logging.error(f"Failed to write to log file: {e}")


def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email)

def validate_csv_row(row):
    errors = []
    if not row.get('subject'):
        errors.append("Missing subject.")
    if not row.get('body'):
        errors.append("Missing Body.")
    if not row.get('to_email') or not is_valid_email(row['to_email']):
        errors.append(f"Missing or Invalid Email: {row.get('to_email')}")
    return errors


def schedule_emails():
    try:
        with open('emails.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                subject = row['subject']
                body = row['body']
                to_email = row['to_email']
                errors = validate_csv_row(row)
                if errors:
                   logging.warning(f"Validatation Errors for row {row}: {', '.join(errors)}")
                   # Skip Invalid Row
                   continue
               
                #schedule tasks
                schedule.every(10).seconds.do(
                    send_email, row['subject'], row['body'], row['to_email']
                )
    except FileNotFoundError:
        logging.error("The CSV file was not Found. Please Ensure it exists.")
    except Exception as e:
        logging.erro(f"An unexpected error occured: {e}")
                

log_file = 'email_log.log'

with open(log_file, "r") as file:
    for line in file:
        #split log line into components
        parts = line.strip().split(" - ", 2)
        if len(parts) == 3:
            timestamp, log_level, message = parts
            print(f"Timestamp: {timestamp}, Level: {log_level}, Message: {message}")
           

schedule_emails()
with open ('emails.csv', mode = 'r') as file:
    reader = csv.DictReader(file)
    print(reader.fieldnames)

#Run the Scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
    
       