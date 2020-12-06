import os
from faker import Faker
from base64 import b64encode
from flog.models import db, Notification, User, Role
from flask import url_for
from flask.ctx import AppContext, RequestContext

fake = Faker()


def login(client: RequestContext, username=os.getenv('FLOG_ADMIN'),
          password=os.getenv('FLOG_ADMIN_PASSWORD')):
    """Login helper function"""
    return client.post(
        "/auth/login/",
        data=dict(username_or_email=username, password=password),
        follow_redirects=True
    )


def logout(client: RequestContext):
    """Logout helper function"""
    return client.get('/auth/logout/', follow_redirects=True)


def register(client: RequestContext, name: str = 'Test', username: str = 'test',
             password: str = 'password', email: str = 'test@example.com'):
    """Register helper function"""
    return client.post('/auth/register/', data=dict(
        name=name,
        username=username,
        email=email,
        password=password,
        password_again=password
    ), follow_redirects=True)


def create_article(client: AppContext) -> dict:
    """Create a post for test use"""
    login(client)
    text = fake.text()
    data = {
        'title': fake.sentence(),
        'content': f"<p>{text}</p>",
    }
    return {
        'response': client.post('/write/', data=data, follow_redirects=True),
        'post': data,
        'text': text,
    }


def send_notification(client: RequestContext) -> None:
    """Send notifications for test user"""
    login(client)
    admin = User.query.filter_by(
        role=Role.query.filter_by(
            name='Administrator'
        ).first()
    ).first()
    notification = Notification(
        message='test',
        receiver=admin
    )
    db.session.add(notification)
    db.session.commit()


def get_api_v1_headers(username: str, password: str) -> dict:
    """Returns auth headers for api v1"""
    return {
        'Authorization': 'Basic ' + b64encode(
            f'{username}:{password}'.encode('utf-8')).decode('utf-8'),
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }


def get_api_v2_headers(client: RequestContext, username, password):
    """Returns auth headers for api v2"""
    response = client.post(url_for('api_v2.oauth_token'), data=dict(
        grant_type='password',
        username=username,
        password=password
    ))
    data = response.get_json()
    token = data.get('access_token')
    return {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
