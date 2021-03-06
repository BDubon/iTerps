from django.urls import path
from .views import register, profile, login_user


app_name = 'users'
urlpatterns = [
    path('', register, name='register'),
    path('/login/', login_user),
    path('<slug:slug>/', profile, name='profile'),
]