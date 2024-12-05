from django.test import TestCase
from django.contrib.auth.models import User
from .models import Playlist, Movie

class PlaylistTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.movie = Movie.objects.create(
            title="Test Movie", description="A test movie", release_date="2024-12-01", poster_url="", backdrop_url="", tmdb_id=1234
        )

    def test_create_playlist(self):
        playlist = Playlist.objects.create(name="My Playlist", user=self.user)
        playlist.movies.add(self.movie)
        self.assertEqual(playlist.movies.count(), 1)
        self.assertEqual(playlist.name, "My Playlist")
