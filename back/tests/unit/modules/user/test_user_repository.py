import pytest
from app.modules.user.infrastructure.repository_sql import UserRepositorySQL
from app.modules.user.domain.entities import User


def test_create_and_list(db):
    repo = UserRepositorySQL(db)
    repo.create(User(None, "Alice", "Smith"))

    users = repo.list()

    assert len(users) == 1
    assert users[0].name == "Alice"
    assert users[0].lastName == "Smith"


def test_created_user_gets_an_id(db):
    repo = UserRepositorySQL(db)
    created = repo.create(User(None, "Bob", "Jones"))

    assert created.id is not None


def test_get_by_id(db):
    repo = UserRepositorySQL(db)
    created = repo.create(User(None, "Carol", "White"))

    found = repo.get_by_id(created.id)

    assert found is not None
    assert found.name == "Carol"


def test_get_by_id_returns_none_when_not_found(db):
    repo = UserRepositorySQL(db)

    assert repo.get_by_id(9999) is None


def test_update(db):
    repo = UserRepositorySQL(db)
    created = repo.create(User(None, "Dave", "Brown"))

    updated = repo.update(User(created.id, "David", "Brown"))

    assert updated.name == "David"


def test_delete(db):
    repo = UserRepositorySQL(db)
    created = repo.create(User(None, "Eve", "Green"))

    repo.delete(created.id)

    assert repo.get_by_id(created.id) is None


def test_count(db):
    repo = UserRepositorySQL(db)
    repo.create(User(None, "Frank", "Gray"))
    repo.create(User(None, "Grace", "Black"))

    assert repo.count() == 2


def test_list_pagination(db):
    repo = UserRepositorySQL(db)
    for i in range(5):
        repo.create(User(None, f"User{i}", "Last"))

    page = repo.list(skip=0, limit=3)

    assert len(page) == 3
