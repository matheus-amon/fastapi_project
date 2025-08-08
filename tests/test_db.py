from dataclasses import asdict
from datetime import datetime

from sqlalchemy import select

from fastzero.models import User


def test_create_user_db(session, mock_db_time):
    with mock_db_time(model=User, time=datetime.now()) as time:
        new_user = User(username='test', email='test@test', password='secret')

        session.add(new_user)
        session.commit()

        user = session.scalar(select(User).where(User.username == 'test'))

        assert asdict(user) == {
            'id': 1,
            'username': 'test',
            'email': 'test@test',
            'password': 'secret',
            'created_at': time,
        }
