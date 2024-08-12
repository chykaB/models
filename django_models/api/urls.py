from django.urls import path
from .views import BookListByAuthor, booklist, index, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path("books_by_author/<str:author_name>", query_book_by_author, name="books_by_author"),
    path("author_and_books/<str:author_name>", BookListByAuthor.as_view(), name="author_and_books"),
    path("books", booklist, name="books"),
    path("", index, name="index"),
    path("register", register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registeration/login.html")),
    path("logout", auth_views.LogoutView.as_view(), name="logout")
]
