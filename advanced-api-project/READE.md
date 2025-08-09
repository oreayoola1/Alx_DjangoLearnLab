# Advanced API Project

## Book API Endpoints
- GET /api/books/ — List all books (public)
- GET /api/books/<id>/ — Retrieve one book (public)
- POST /api/books/create/ — Create a book (authenticated)
- PUT/PATCH /api/books/<id>/update/ — Update a book (authenticated)
- DELETE /api/books/<id>/delete/ — Delete a book (authenticated)

## Permissions
- Public can read data.
- Only logged-in users can create, update, or delete.