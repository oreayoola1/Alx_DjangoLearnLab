from django.urls import path
from django.views.generic.base import RedirectView
from .views import BlogLoginView, BlogLogoutView, register, profile
from django.contrib.auth.decorators import login_required
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    # Backwards-compatible singular URLs -> redirect to canonical plural URLs
    path('post/new/', RedirectView.as_view(pattern_name='post-create', permanent=False)),
    path('post/<int:pk>/update/', RedirectView.as_view(pattern_name='post-update', permanent=False)),
    path('post/<int:pk>/delete/', RedirectView.as_view(pattern_name='post-delete', permanent=False)),
    path("login/", BlogLoginView.as_view(), name="login"),
    path("logout/", BlogLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", login_required(profile), name="profile"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]