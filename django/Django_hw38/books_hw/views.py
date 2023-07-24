from django.http import JsonResponse
from .models import Book

def books_view(request):
    books = Book.objects.all()
    data = [{"id": book.id, "title": book.title, "author": book.author} for book in books]
    return JsonResponse(data, safe=False)