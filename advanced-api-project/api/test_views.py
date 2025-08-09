# api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()

        # Create test author and books
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(
            title="Harry Potter and the Sorcerer's Stone",
            author=self.author,
            publication_year=1997
        )
        self.book2 = Book.objects.create(
            title="Harry Potter and the Chamber of Secrets",
            author=self.author,
            publication_year=1998
        )

        # URLs
        self.list_url = reverse('book-list')  # /books/
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})

    def test_list_books(self):
        """Test retrieving all books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        """Test creating a book with authentication"""
        self.client.login(username='testuser', password='password123')
        data = {
            "title": "Harry Potter and the Prisoner of Azkaban",
            "author": self.author.id,
            "publication_year": 1999
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Ensure unauthenticated users cannot create books"""
        data = {
            "title": "Unauthorized Book",
            "author": self.author.id,
            "publication_year": 2000
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Test updating a book with authentication"""
        self.client.login(username='testuser', password='password123')
        data = {
            "title": "Harry Potter and the Sorcerer's Stone - Updated",
            "author": self.author.id,
            "publication_year": 1997
        }
        response = self.client.put(self.detail_url(self.book1.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, data['title'])

    def test_delete_book_authenticated(self):
        """Test deleting a book with authentication"""
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_year(self):
        """Test filtering books by publication year"""
        response = self.client.get(f"{self.list_url}?publication_year=1997")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book1.title)

    def test_search_books(self):
        """Test searching books by title"""
        response = self.client.get(f"{self.list_url}?search=Chamber")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book2.title)

    def test_order_books_by_year_desc(self):
        """Test ordering books by publication year in descending order"""
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data[0]['publication_year'], response.data[1]['publication_year'])
