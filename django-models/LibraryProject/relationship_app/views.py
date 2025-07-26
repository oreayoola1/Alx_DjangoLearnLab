from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})
from django.views.generic import DetailView
from .models import Library  # ✅ import is required

class LibraryDetailView(DetailView):
    model = Library  # ✅ model reference
    template_name = "relationship_app/library_detail.html"  # ✅ template path
    context_object_name = "library"  # ✅ variable expected in template
