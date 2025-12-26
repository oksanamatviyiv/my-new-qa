import pytest
from conftest import User


@pytest.mark.check
def test_change_name(user: User):
    assert user.name == "Oksana"


@pytest.mark.check
def test_change_second_name(user: User):
    assert user.second_name == "Matviyiv"
