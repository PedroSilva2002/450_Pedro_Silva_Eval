from django.test import TestCase, Client
from django.urls import reverse
from library.models import Book

class BookIntegrationTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a book to be deleted in each test method
        cls.book = Book.objects.create(author="Dominique Roques", title="Pico Bogue")

    def test_delete_book(self):
        # Act: Send a POST request to delete the book
        client = Client()
        print("Book Title before deletion:", self.book.title)
        response = client.post(reverse('delete_book', args=[self.book.id]))

        # Print the status code
        print("Status code:", response.status_code)

        # Assert
        # Redirect to the appropriate page after deletion (in this case, the index page)
        self.assertRedirects(response, reverse('index'), status_code=302, target_status_code=200)

        # Check that the book has been deleted from the database
        book_exists = Book.objects.filter(id=self.book.id).exists()
        self.assertFalse(book_exists, "The book was not deleted from the database.")
