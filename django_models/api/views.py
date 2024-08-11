from django.shortcuts import render
from django.http import Http404
from .models import Author, Book
from django.views import View

# Create your views here.
# def query_book_by_author(request, author_name):
#     author = Author.objects.get(name=author_name)
#     books = Book.objects.filter(author=author)
#     context = {
#         "books": books
#     }
#     return render(request, "book_by_author.html", context)

def booklist(request):
    books = Book.objects.all()
    return render(request, "book_by_author.html", {"books":books})

class BookListByAuthor(View):
    def get(self, request, author_name): 
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return render(request, "book_by_author.html", {"books":books})