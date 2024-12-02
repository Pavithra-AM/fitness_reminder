from django.contrib import admin
from django.urls import path, include  # include is important!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reminder.urls')),  # This routes to your app
]
