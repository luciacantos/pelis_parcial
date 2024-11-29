from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from streaming.models import Movie
from streaming.serializers import MovieSerializer

class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

class MovieDetailView(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

