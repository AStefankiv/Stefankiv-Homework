from django.http import JsonResponse
from .models import Book

def book_list_json(request):
    books = Book.objects.all()

    books_json = [{"title": book.title, "author": book.author, "published_date": book.published_date} for book in books]

    return JsonResponse(books_json, safe=False)