from .models import Author, Book, Library

# ===== Author and Books by Author =====
author_name = "Chinua Achebe"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

for book in books_by_author:
    print(book.title)

# ===== Library and Books in Library =====
library_name = "National Library"
library = Library.objects.get(name=library_name)

# Access all books in the library (assuming a ManyToMany or related_name='books')
books_in_library = library.books.all()  # <-- This line is required by checker

for book in books_in_library:
    print(book.title)
