from django.urls import path
from .views import BooksView, BookDetailView, CreateBookView

urlpatterns = [
    path('books/', BooksView.as_view(), name='books_list'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book_detail'),
    path('books/create/', CreateBookView.as_view(), name='create_book'),
]
