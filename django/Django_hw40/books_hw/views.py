from django.shortcuts import render, redirect
from django.views import View
from .models import Book
from .forms import BookForm

class BooksView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'books_list.html', {'books': books})

class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(pk=id)
        return render(request, 'book_detail.html', {'book': book})

class CreateBookView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'create_book.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_list')
        return render(request, 'create_book.html', {'form': form})
