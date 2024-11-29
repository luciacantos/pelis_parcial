from django.urls import path
from .views import MovieListView, MovieDetailView, home

urlpatterns = [
    path('', home, name='home'),
    path('api/movies/', MovieListView.as_view(), name='movie-list'),
    path('api/movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
]
