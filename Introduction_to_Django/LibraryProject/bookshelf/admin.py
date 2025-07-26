from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these columns
    list_filter = ('publication_year',)                     # Add a filter for years
    search_fields = ('title', 'author')                     # Enable search
