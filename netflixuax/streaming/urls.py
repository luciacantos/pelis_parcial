from django.urls import path
from .views import MovieListView, MovieDetailView, PlaylistView, RecommendationView, home

urlpatterns = [
    path('', home, name='home'),
    path('api/movies/', MovieListView.as_view(), name='movie-list'),
    path('api/movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('api/playlists/', PlaylistView.as_view(), name='playlist'),
    path('api/recommendations/', RecommendationView.as_view(), name='recommendation'),
]
