from django.urls import path
from .views import register, profile


app_name = 'courses'
urlpatterns = [
    path('', register, name='register'),
    path('<slug:slug>/', profile, name='profile'),
]