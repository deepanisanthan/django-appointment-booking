from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for Django Admin
    path('api/', include('your_app.urls')),  # Include URLs for your custom app (e.g., 'appointments')
]
