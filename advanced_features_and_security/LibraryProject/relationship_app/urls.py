from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Book operations
    path('books/', views.list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),

    # Library detail
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based views
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
    
     # Book management URLs (required)
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),

    # Optional: other views that are useful
    path('books/', views.list_books, name='list_books'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
