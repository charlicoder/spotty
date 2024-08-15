from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'about']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'publisher', 'series_name', 'average_rating']