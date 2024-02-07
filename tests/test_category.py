import pytest

from product.factories import CategoryFactory


@pytest.fixture
def category():
    return CategoryFactory()


@pytest.mark.django_db
def test_create_category(category):
    assert category.title is not None
    assert category.slug is not None
    assert category.description is not None
    assert category.active
