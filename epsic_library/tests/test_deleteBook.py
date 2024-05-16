import pytest
from library.models import Book
from django.test import Client, TestCase
from django.core.exceptions import ObjectDoesNotExist


class BookDelete(TestCase):

    @classmethod
    def setUpTestData(cls):
        Book.objects.create(author="Dominique Roques", title="Pico Bogue")

    @pytest.mark.django_db
    def test_delete_book_with_admin_interface(self):
        book = Book.objects.get(id=1)
        print(book.title)
        book.delete()

        # Attempt to retrieve the deleted book, should raise DoesNotExist exception
        try:
            deleted_book = Book.objects.get(id=1)
            book_exists = True
        except ObjectDoesNotExist:
            book_exists = False

        assert not book_exists
