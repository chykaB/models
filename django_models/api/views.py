from django.shortcuts import render, redirect
from .models import Author, Book
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # auth_login(request, user)
            # return redirect(request,"books")
    else:
        form = UserCreationForm()
    return render(request, "registeration/register.html", {"form":form})

            
        





# Create your views here.
# def query_book_by_author(request, author_name):
#     author = Author.objects.get(name=author_name)
#     books = Book.objects.filter(author=author)
#     context = {
#         "books": books
#     }
#     return render(request, "book_by_author.html", context)

def booklist(request):
    books = Book.objects. all()
    return render(request, "book_by_author.html", {"books":books})

class BookListByAuthor(View):
    def get(self, request, author_name): 
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return render(request, "book_by_author.html", {"books":books})