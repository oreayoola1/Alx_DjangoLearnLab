from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "Chinua Achebe"
books_by_author = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}:", books_by_author)

# 2. List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}:", books_in_library)

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library__name=library_name)
print(f"Librarian at {library_name}:", librarian)
