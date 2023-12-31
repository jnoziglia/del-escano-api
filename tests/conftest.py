from api import create_app, db
from api.model.party import Party
from api.model.history import History
from api.model.user import User
import pytest
import jwt


@pytest.fixture
def app():
    app = create_app(test_config={
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'TESTING': True,
        'DEBUG': False,
        'SQLALCHEMY_ECHO': False
    })
    with app.app_context():
        db.init_app(app)
        db.create_all()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def populate_party(app):
    with app.app_context():
        parties = [
            Party(name='partyA', votes=340000),
            Party(name='partyB', votes=280000),
            Party(name='partyC', votes=160000),
            Party(name='partyD', votes=60000),
            Party(name='partyE', votes=15000)
        ]
        db.session.add_all(parties)
        db.session.commit()
        return parties


@pytest.fixture
def populate_history(app):
    with app.app_context():
        history = History(seat_count=7, result=[
                          {'id': 1, 'name': 'partyA', 'votes': 340000, 'seats': 3},
                          {'id': 2, 'name': 'partyB', 'votes': 280000, 'seats': 3},
                          {'id': 3, 'name': 'partyC', 'votes': 160000, 'seats': 1},
                          {'id': 4, 'name': 'partyD', 'votes': 60000, 'seats': 0},
                          {'id': 5, 'name': 'partyE', 'votes': 15000, 'seats': 0}
                          ])
        db.session.add(history)
        db.session.commit()


@pytest.fixture
def token(app):
    with app.app_context():
        user = User(email='test@test.com', password='test')
        db.session.add(user)
        db.session.commit()
        token = jwt.encode(
            {"user_id": user.id},
            app.config["SECRET_KEY"],
            algorithm="HS256"
        )
    return token
