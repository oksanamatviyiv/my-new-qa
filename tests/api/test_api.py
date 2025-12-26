import pytest

from conftest import User


@pytest.mark.change
def test_remove_name(user: User):
    user.name = ""
    assert user.name == ""


@pytest.mark.check
def test_name(user: User):
    assert user.name == "Oksana"


@pytest.mark.check
def test_second_name(user: User):
    assert user.second_name == "Matviyiv"
