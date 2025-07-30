from django.contrib import admin
from django.urls import path, include
from relationship_app import views as relationship_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),
    path('', relationship_views.home, name='home'),  # This line fixes the 404
]
