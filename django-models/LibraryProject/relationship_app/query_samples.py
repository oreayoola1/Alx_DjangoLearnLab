from .models import Author, Book, Library, Librarian

# ===== Author and Books by Author =====
author_name = "Chinua Achebe"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

for book in books_by_author:
    print(book.title)

# ===== Library and Books in Library =====
library_name = "National Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()  # assumes ManyToManyField or related_name='books'

for book in books_in_library:
    print(book.title)

# ===== Librarian Assigned to Library =====
librarian = Librarian.objects.get(library=library)
print(f"Librarian: {librarian.name}")
