import pytest
from unittest.mock import MagicMock
from app.modules.user.application.use_cases.create_user import CreateUserUseCase
from app.modules.user.domain.entities import User


def make_use_case():
    repo = MagicMock()
    return CreateUserUseCase(repo), repo


def test_create_user_success():
    use_case, repo = make_use_case()
    repo.create.return_value = User(1, "Alice", "Smith")

    result = use_case.execute("Alice", "Smith")

    assert result.name == "Alice"
    assert result.lastName == "Smith"
    repo.create.assert_called_once()


def test_create_user_short_name_raises():
    use_case, _ = make_use_case()

    with pytest.raises(ValueError, match="3 characters"):
        use_case.execute("Al", "Smith")


def test_create_user_short_last_name_raises():
    use_case, _ = make_use_case()

    with pytest.raises(ValueError, match="3 characters"):
        use_case.execute("Alice", "Sm")


def test_create_user_empty_name_raises():
    use_case, _ = make_use_case()

    with pytest.raises(ValueError):
        use_case.execute("", "Smith")


def test_create_user_empty_last_name_raises():
    use_case, _ = make_use_case()

    with pytest.raises(ValueError):
        use_case.execute("Alice", "")