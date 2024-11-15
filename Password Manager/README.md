# Password Manager  

## Description  
This **Password Manager** is a secure, web-based application developed using Python, Flask, and SQL. It is designed to help users securely store, retrieve, and manage their passwords. The system incorporates strong encryption techniques to ensure data privacy and security.  

The project demonstrates skills in full-stack development, focusing on robust backend architecture, database integration, and responsive user interface design.

---

## Features  
### Core Functionality:  
- **User Authentication:**  
  - Secure user registration and login system.  
  - Password hashing with bcrypt for storing user credentials securely.  
- **Password Storage:**  
  - Encrypts stored passwords using AES encryption.  
  - Ability to add, edit, and delete stored entries.  
- **Search & Filtering:**  
  - Quickly locate saved passwords by account name or category.  
- **Responsive Design:**  
  - Mobile-friendly interface using Bootstrap for an intuitive user experience.  

### Security Practices:  
- **Encryption:** All passwords are encrypted before being stored in the database.  
- **Session Management:** User sessions are secured using Flask-Login and CSRF protection.  
- **Data Validation:** Input fields are sanitized to prevent SQL injection and XSS attacks.  

---

## Technologies Used  
- **Backend:** Python, Flask  
- **Frontend:** HTML5, CSS, JavaScript, Bootstrap  
- **Database:** SQLAlchemy ORM with SQLite  
- **Security:**  
  - AES Encryption (via Python's Cryptography library)  
  - Bcrypt for password hashing  

---

## Setup Instructions  

### Prerequisites:  
Ensure you have the following installed:  
- Python 3.8+  
- Pip (Python package manager)  

### Steps:  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/shannonmceld/Portfolio-/tree/main/Password%20Manager  

	2.	Navigate to the project directory:

cd Password-Manager  


	3.	Install required dependencies:

pip install -r requirements.txt  


	4.	Initialize the database:

python setup_db.py  


	5.	Run the Flask application:

python app.py  


	6.	Open your web browser and access the application at:

http://127.0.0.1:5000  

Screenshots

Login Page

Dashboard

Add New Password

Project Structure

Password-Manager/  
│  
├── app.py               # Main Flask application  
├── setup_db.py          # Database initialization script  
├── static/              # Static files (CSS, JS, images)  
│   ├── css/  
│   └── js/  
├── templates/           # HTML templates  
│   ├── login.html  
│   ├── dashboard.html  
│   └── add_password.html  
├── requirements.txt     # Python dependencies  
├── README.md            # Project documentation  
└── database.db          # SQLite database (created during setup)  

Future Improvements

	•	Multi-Factor Authentication: Enhance account security with two-factor authentication.
	•	Password Generator: Integrate a feature to generate strong, random passwords.
	•	User Roles: Add support for multi-user accounts with varying access levels.
	•	Cloud Hosting: Deploy the application to a cloud platform like AWS or Heroku.

Contact

This project was created by Shannon McElderry.
Feel free to reach out with feedback or sugestions!
