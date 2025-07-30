from bookshelf.models import Book

# Delete a book with a specific ID
book = Book.objects.get(id=1)
book.delete()
