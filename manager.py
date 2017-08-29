#manager.py

from flask_script import Manager
from project import create_app, db
from project.api.models import User
import unittest

app = create_app()
manager = Manager(app)
@manager.command
def test():
    """Runs the tests without code coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def recreate_db():
    """Recreates a database."""
    db.drop_all()
    db.create_all()
    db.session.commit()

def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user

@manager.command
def seed_db():
    """Seeds the database."""
    db.create_all()
    db.session.commit()
    add_user('michael', 'michael@realpython.com')
    add_user('michaelherman', 'michael@mherman.org')
    db.session.commit()


if __name__ == '__main__':
	manager.run()
