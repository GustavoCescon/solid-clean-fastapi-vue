import pytest
from unittest.mock import MagicMock
from app.modules.auth.application.use_cases.login import LoginUseCase
from app.core.errors.base import AppException


def make_use_case(user=None):
    repo = MagicMock()
    repo.find_by_email.return_value = user
    return LoginUseCase(repo)


def test_login_success():
    user = MagicMock()
    user.id = 1
    user.password = "secret"
    use_case = make_use_case(user)

    result = use_case.execute("test@mail.com", "secret")

    assert "access_token" in result
    assert isinstance(result["access_token"], str)


def test_login_user_not_found_raises_401():
    use_case = make_use_case(None)

    with pytest.raises(AppException) as exc_info:
        use_case.execute("unknown@mail.com", "any")

    assert exc_info.value.status_code == 401


def test_login_wrong_password_raises_401():
    user = MagicMock()
    user.id = 1
    user.password = "correct"
    use_case = make_use_case(user)

    with pytest.raises(AppException) as exc_info:
        use_case.execute("test@mail.com", "wrong")

    assert exc_info.value.status_code == 401
