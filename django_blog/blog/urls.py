from django.urls import path
from django.views.generic.base import RedirectView
from .views import BlogLoginView, BlogLogoutView, register, profile
from django.contrib.auth.decorators import login_required
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView,
    TagPostListView, search,
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    # Backwards-compatible singular URLs -> redirect to canonical plural URLs
    path('post/new/', RedirectView.as_view(pattern_name='post-create', permanent=False)),
    path('post/<int:pk>/update/', RedirectView.as_view(pattern_name='post-update', permanent=False)),
    path('post/<int:pk>/delete/', RedirectView.as_view(pattern_name='post-delete', permanent=False)),
    # Backwards-compatible comment URL aliases
    path('post/<int:post_pk>/comments/new/', RedirectView.as_view(pattern_name='comment-create', permanent=False)),
    path('post/<int:pk>/comments/new/', RedirectView.as_view(pattern_name='comment-create', permanent=False)),
    path('comment/<int:pk>/update/', RedirectView.as_view(pattern_name='comment-update', permanent=False)),
    path('comment/<int:pk>/delete/', RedirectView.as_view(pattern_name='comment-delete', permanent=False)),
    path("login/", BlogLoginView.as_view(), name="login"),
    path("logout/", BlogLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", login_required(profile), name="profile"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:post_pk>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-update"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
    path('tags/<str:tag_name>/', TagPostListView.as_view(), name='tag-posts'),
    path('search/', search, name='search'),
]