from django.urls import path
from .views import (
    BookListCreateView,
    BookRetrieveUpdateDeleteView
)

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-detail'),
]