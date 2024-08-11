from django.urls import path
from .views import BookListByAuthor, booklist
urlpatterns = [
    # path("books_by_author/<str:author_name>", query_book_by_author, name="books_by_author"),
    path("author_and_books/<str:author_name>", BookListByAuthor.as_view(), name="author_and_books"),
    path("books", booklist, name="books")
]
