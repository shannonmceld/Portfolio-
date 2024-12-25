import pytest
from app import app,db
from models import Tasks
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()
    
    
@pytest.fixture
def sample_task():
    return {
        'title': 'Test Task',
        'description': 'This is a Test',
        'email': 'test@example.com',
        'due_date': datetime(2024, 12, 25, 10, 0, 0),
        'reminder_time': datetime(2024, 12, 25, 10, 0, 0),
        'completed': 'False',
        "user_id": 1
    }
            
            
def test_create_task(client):
    sample_task = {
        'title': 'Test Task',
        'description': 'This is a Test',
        'email': 'test@example.com',
        'due_date': datetime(2024, 12, 25, 10, 0,0),
        'reminder_time': datetime(2024, 12, 25, 10, 0,0),
        "completed": False,
        "user_id": 1
    }   
    response = client.post ('/create', data=sample_task, follow_redirects=True)
    assert response.status_code == 200, "Post request failed"
    
    with app.app_context():   
        task = Tasks.query.filter_by(title='test task').first()
        print(task)
        assert task is not None, "Task was not created"
        assert task.title == 'test task'
    
    
def test_view_tasks(client):
    task = Tasks(
        title='View Test',
        description='Test Description',
        email='view@test.com',
        due_date= datetime(2024, 12, 25, 10, 0,0),
        reminder_time= datetime(2024, 12, 25, 10, 0,0),
        user_id= 1
    )
    db.session.add(task)
    db.session.commit()
    response = client.get('/view_tasks')
    assert response.status_code == 200
    assert b"View Test" in response.data
    
    
def test_update_task(client):
    task = Tasks(
        title='update Test',
        description='Update Description',
        email='update@test.com',
        due_date= datetime(2024, 12, 25, 10, 0, 0),
        reminder_time= datetime(2024, 12, 25, 10, 0, 0),
        user_id= 1
    )
    db.session.add(task)
    db.session.commit()
    response = client.post(f'/update/{task.id}', data={
        'title': 'Update Task',
        'description': 'Update Description',
        'email': 'update@example.com',
        'due_date': datetime(2024, 12, 25, 10, 0, 0),
        'reminder_time': datetime(2024, 12, 25, 10, 0, 0),
        'user_id' : 1
    }, follow_redirects=True)
    assert response.status_code == 200
    updated_task = Tasks.query.get(task.id)
    assert updated_task.title =='Updated Task'
    
def test_delete_task(client):
    task = Tasks(
        title='Delete Test',
        description='Delete Description',
        email='delete@test.com',
        due_date=datetime(2024, 12, 25, 10, 0, 0),
        reminder_time=datetime(2024, 12, 25, 10, 0, 0),
        user_id= 1
    )
    db.session.add(task)
    db.session.commit()
    response = client.post(f'/delete/{task.id}', follow_redirects=True)
    assert response.status_code == 200
    deleted_task = Tasks.query.get(task.id)
    assert deleted_task is None
        
        