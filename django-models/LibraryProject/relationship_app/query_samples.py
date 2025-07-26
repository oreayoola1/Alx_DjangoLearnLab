from .models import Author, Book

# Sample variable
author_name = "Chinua Achebe"

# Get the Author object by name
author = Author.objects.get(name=author_name)

# Get all books written by that author
books_by_author = Book.objects.filter(author=author)

# Print result (for testing purpose)
for book in books_by_author:
    print(book.title)
