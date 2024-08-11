from django.contrib import admin
from .models import Author, Book, Librarian, Library
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
admin.site.register(Librarian)
admin.site.register(Library)
