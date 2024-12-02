from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_reminder, name='home'),  # Home page
    path('new-reminder/', views.get_new_reminder, name='new_reminder'),  # API for new reminder
]
