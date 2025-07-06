import pytest
from database import Database

@pytest.fixture
def db():
    database = Database()
    yield database
    database.data.clear()

def test_add_user(db):
    db.add_user(1,"Alice")
    db.get_user(1) == "Alice" 
 
def test_add_user_exists(db):
    db.add_user(1,"Alice")
    with pytest.raises(ValueError,match="User already exists"):
        db.add_user(1,"Alice")

def test_delete_user(db):
    db.add_user(1,"Alice")
    assert db.get_user(1) == "Alice"
    db.delete_user(1)
    with pytest.raises(ValueError) as info_error:
        db.get_user(1)