from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeLocalField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo, Length, InputRequired
from datetime import datetime


class ForgotPasswordForm(FlaskForm):
    email = StringField(
        'Email', 
        validators=[InputRequired(), Email()]
    )
    new_password = PasswordField(
        'New Password',
        validators=[InputRequired(), Length(min=6)]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('new_password', message='Passwords must Match')]
    )
    submit = SubmitField(
        'Reset Password'
    )

class LoginForm(FlaskForm):
    email = StringField(
        'Email', 
        validators=[InputRequired(), Email()]
    )
    password = PasswordField(
        'Password',
        validators=[InputRequired()]
    )
    submit = SubmitField(
        'Login In'
    )
    
    
class RegistrationForm(FlaskForm):
    username = StringField(
        'Username', 
        validators=[DataRequired(), Length(min=3, max=80)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email(), Length(min=3, max=80)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=6)]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password', message='Passwords must Match')]
    )
    submit = SubmitField(
        'Register'
        )
    
    
    
class TaskForm(FlaskForm):
    title = StringField(
        'Task Title', 
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter the task Title (e.g, Submit report)"}
        )
    description = TextAreaField(
        'Task Description',
        render_kw={"placeholder": "Add details about the task"}
        )
    email = StringField(
        'Email', 
        validators=[DataRequired(), Email(message="Invalid email Address")],
        render_kw={"placeholder": "Enter your email for reminders"}
        )
    due_date = DateTimeLocalField(
        'Due Date (YYYY-MM-DD HH:MM)', 
        validators=[DataRequired()], 
        format='%Y-%m-%dT%H:%M',
        render_kw={"placeholder": "YYYY-MM-DD HH:MM"}
        )
    reminder_time = DateTimeLocalField(
        'Reminder Time (YYYY-MM-DD HH:MM)', 
        validators=[DataRequired()], 
        format='%Y-%m-%dT%H:%M',
        render_kw={"placeholder":"YYYY-MM-DD HH:MM"}
        )
    completed = BooleanField(
        "Completed"
    )
    
    def validate_due_date(form, field):
        if field.data <= datetime.now():
            raise ValidationError('Due Date must be in the Future.')

    def validate_reminder_time(form, field):
        if field.data <= datetime.now():
            raise ValidationError('Reminder Time must be in the Future.')
        
    submit = SubmitField(
        'Create Task'
        )