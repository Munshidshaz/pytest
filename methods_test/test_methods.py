import pytest
from method import UserManager


@pytest.fixture
def user_manager():
    """Create a fresh instance of usermanager before each test"""
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("john_doe", "john@example.com") == True
    assert user_manager.get_user("john_doe") == "john@example.com"

def test_unkownUser_get(user_manager):
    with pytest.raises(ValueError, match="User not found"):
        user_manager.get_user("John_doe")

def test_duplicate_user(user_manager):
    user_manager.add_user("john_doe", "john@example.com")
    with pytest.raises(ValueError,match="User already exists"):
        user_manager.add_user("john_doe", "john@example.com")