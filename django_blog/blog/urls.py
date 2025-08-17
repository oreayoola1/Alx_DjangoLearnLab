from django.urls import path
from .views import BlogLoginView, BlogLogoutView, register, profile
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("login/", BlogLoginView.as_view(), name="login"),
    path("logout/", BlogLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", login_required(profile), name="profile"),
]