import pytest
from unittest.mock import patch
from library.views import book_list


@pytest.mark.django_db
@patch('library.views.Book.objects.all')
def test_book_list_view(mocker):
    # Arrange
    mocked_books = [
        {'author': 'Dominique Roques', 'title': 'Pico Bogue'},
        {'author': 'J.K. Rowling', 'title': 'Harry Potter'},
    ]
    mocker.return_value = mocked_books

    # Act
    response = book_list(None)

    # Assert
    assert response.status_code == 200
    assert 'Dominique Roques | Pico Bogue' in response.content.decode()
    assert 'J.K. Rowling | Harry Potter' in response.content.decode()
