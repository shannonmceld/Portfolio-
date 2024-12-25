from flask import Flask, render_template, redirect, url_for, flash, request, session
from forms import TaskForm, RegistrationForm, LoginForm, ForgotPasswordForm
from flask_apscheduler import APScheduler
from datetime import datetime
from models import Users, Tasks, db
import time
from send_email import send_email, os
import logging
import threading
import schedule
from flask_login import current_user, LoginManager, login_user, logout_user, login_required
from bcrypt import checkpw


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_BINDS'] = {'tasks': 'sqlite:///tasks.db'}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY', 'default_secret')
db.init_app(app)  


already_logged = set()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s", 
    handlers=[
        logging.FileHandler("email_errors.log"),
        logging.StreamHandler()
    ]
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return db.session.query(Users).filter_by(id=user_id).first()

def log_once(message, level=logging.INFO and logging.ERROR):
    global logged_messages
    if (message, level) not in logged_messages:
        logging.log(level,message)
        logged_messages.add(message,level)
        

class Config:
    SCHEDULER_API_ENABLED = True
    
app.config.from_object(Config)
scheduler = APScheduler()


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    form = ForgotPasswordForm() 
    if form.validate_on_submit():
        # Query the user by email 
        email = form.email.data.strip()
        new_password = form.new_password.data.strip()
        user = Users.query.filter_by(email=email).first()
        if user:
            user.set_password(new_password)
            db.session.commit()
            
            flash('Your password has been reset!', 'success') 
            return redirect(url_for('login'))
        else:
            flash('No such email', 'error') 
            return redirect(url_for('forgot_password'))
    return render_template("forgot_password.html", form=form)


@app.route('/login', methods=['GET', 'POST']) 
def login():
    form = LoginForm() 
    if form.validate_on_submit(): 
    # Query the user by email 
        email = form.email.data.strip()
        user = Users.query.filter_by(email=email).first() 
        if user and checkpw(form.password.data.encode('utf-8'), user.hash_password.encode('utf-8')):
            # Remember which user has logged in
            login_user(user)
            logging.info(f'user{user}{user.id}{session}{current_user.is_authenticated}')
            flash('Login successful!', 'success') 
            return redirect(url_for('view_task')) 
        else: flash('Invalid email or password.', 'error') 
    return render_template('login.html', form=form)
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            # Check if username or email already exists
            existing_user = Users.query.filter((Users.username == form.username.data) | (Users.email == form.email.data)).first()
            if existing_user:
                flash('username or Email already exists.', 'error')
                return redirect(url_for('register'))
            
            # create a new user
            new_user = Users(
                username=form.username.data.strip(),
                email=form.email.data.strip()
            )
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            logging.info(f'user{new_user}{new_user.id}{session}{current_user.is_authenticated}')
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('view_task')) 
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred: {e}", 'error')
            
    return render_template('register.html', form=form)
            

@app.route('/view')
@login_required
def view_task():
    tasks = Tasks.query.filter_by(user_id=current_user.id).all()
    return render_template('view_task.html', tasks=tasks)
       
@app.route('/delete/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Tasks.query.get_or_404(task_id)
    try:
        db.session.delete(task)
        db.session.commit()
        flash("Task deleted successfully!", 'success')
    except Exception as e:
            db.session.rollback()
            flash(f"Error deleting task: {e}", 'error') 
    return redirect(url_for('view_task'))

@app.route('/update<int:id>', methods=['GET', 'POST'])
@login_required
def update_task(id):
    tasks = Tasks.query.get_or_404(id)
    form = TaskForm(obj=tasks)
    if form.validate_on_submit():
        try:
            tasks.title = form.title.data.strip()
            tasks.description = form.description.data.strip()
            tasks.email = form.email.data.strip()
            tasks.due_date = form.due_date.data
            tasks.reminder_time = form.reminder_time.data
            tasks.completed = form.completed.data
            
            db.session.commit()
            flash("Task updated successfully!", 'success')
            return redirect(url_for('view_task'))
        except Exception as e:
            db.session.rollback()
            flash(f"An error occured: {e}", 'error')
            
    return render_template('update_task.html', form=form, tasks=tasks)

@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_task():
    app.debug = True
    form = TaskForm()
    if form.validate_on_submit():
        logging.info(f'user{current_user.id}')
        try:
            app.logger.info("Form submitted with valid data")
        # Create a new task instance
            new_task = Tasks(
                title = form.title.data.strip(),
                description = form.description.data.strip(),
                email = form.email.data.strip(),
                due_date=form.due_date.data,
                reminder_time = form.reminder_time.data,
                completed = form.completed.data,
                user_id=current_user.id # Assign the task to the current user
            )
            # Add to the database
            db.session.add(new_task)
            db.session.commit()
            flash('Task created successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f"an error occurred: {e}", 'error')

    else:
        if form.errors: # Add feedback if form validator fails
            app.logger.warning("Form validation errors: {form.errors}")
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Error in {field}: {error}", 'error' )
    return render_template('create_task.html', form=form)

@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()
    logout_user()
    flash("You have been logged out.", "info")
    # Redirect user to login form
    return redirect(url_for('login'))


# debug the scheduler
def run_scheduler():
    with app.app_context():
        app.logger.info("Scheduler is Starting.....")
        schedule.every(1).minute.do(send_reminder)
        while True:
            try:
                schedule.run_pending()
                time.sleep(1)
            except Exception as e:
                app.logger.error(f"Error in Scheduler: {e}")

def send_reminder():
    # simulate email sending
    now = datetime.now()
    tasks = Tasks.query.filter(Tasks.reminder_time <= now, ~Tasks.completed).all()
    for task in tasks:
        try:
            send_email(task)
            task.completed = True
            db.session.commit()
            logging.info(f"Reminder email sent successfully to: {task.title}") 
        except Exception as e:
            logging.error(f"Failed to send reminder for task {task.title}: {e}")
            print(f"Reminder sent for task: '{task.title}' to {task.email}")
    return "Reminders sent!"

if __name__ == "__main__":
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()
    
    
    app.run(debug=True)
    



    
