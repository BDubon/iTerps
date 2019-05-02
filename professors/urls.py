from django.urls import path
from .views import (ProfessorListView, ProfessorDetailView)

app_name = 'professors'
urlpatterns = [
    path('', ProfessorListView.as_view(), name='professor_list'),
    path('<slug:slug>/', ProfessorDetailView.as_view(), name='professor_detail'),
]