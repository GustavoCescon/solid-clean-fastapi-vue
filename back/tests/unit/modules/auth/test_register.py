import pytest
from unittest.mock import MagicMock
from app.modules.auth.application.use_cases.register import RegisterUseCase
from app.core.errors.base import AppException


def make_use_case(existing_user=None):
    repo = MagicMock()
    repo.find_by_email.return_value = existing_user
    repo.create_auth.return_value = MagicMock(id=1, email="test@mail.com")
    return RegisterUseCase(repo)


def test_register_success():
    use_case = make_use_case(None)

    result = use_case.execute("testuser", "test@mail.com", "password")

    assert result is not None
    assert result.email == "test@mail.com"


def test_register_creates_auth_in_repo():
    repo = MagicMock()
    repo.find_by_email.return_value = None
    repo.create_auth.return_value = MagicMock()
    use_case = RegisterUseCase(repo)

    use_case.execute("user", "new@mail.com", "pass")

    repo.create_auth.assert_called_once_with("user", "new@mail.com", "pass")


def test_register_duplicate_email_raises_409():
    use_case = make_use_case(existing_user=MagicMock())

    with pytest.raises(AppException) as exc_info:
        use_case.execute("user", "dup@mail.com", "pass")

    assert exc_info.value.status_code == 409
