from django.db import models

# Create your models here.

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    poster_url = models.URLField()
    backdrop_url = models.URLField()
    tmdb_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.title

