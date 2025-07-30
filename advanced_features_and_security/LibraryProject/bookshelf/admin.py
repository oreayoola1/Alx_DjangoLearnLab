from django.contrib import admin
from .models import Book
from .models import CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # remove 'publication_year'
    list_filter = ()                    # or remove this line entirely if unused
    search_fields = ('title', 'author')