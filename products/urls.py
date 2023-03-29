from django.urls import path
from . import views

urlpatterns = [
    path('artworks/', views.artworks_view, name='artworks'),
]