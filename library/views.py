from django.shortcuts import get_object_or_404, render, redirect
from django.views import View

from .models import Book

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_visits': num_visits},
    )

def book_info(request, pk):
    """View function for book info."""
    book = get_object_or_404(Book, pk=pk)
    return render(request, "book_info.html", {'book':book})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

class DeleteBookView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'delete_book.html', {'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('index')

