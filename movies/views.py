from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, Request, status
from rest_framework import permissions

from .models import Movie
from .serializer import MovieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import(
    IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly)
from users.permission import IsAdminOrReadOnly, IsAdminWithReadAccess
from movies.permission import IsEmployee, IsSuperUserOrRead
from rest_framework.decorators import permission_classes

    
class MovieView(APIView):
    permission_classes = [IsAdminWithReadAccess]
    authentication_classes = [JWTAuthentication]
    def get(self, request: Request)-> Response:
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request: Request) -> Response:
        
        serializer = MovieSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        
       
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class OtherMovieIdView(APIView):
    
    def get(self, request: Request, id=int) -> Response:
        movie = get_object_or_404(Movie, id=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    @permission_classes([IsEmployee])
    def delete(self, request: Request, id=int):
        movie_del = get_object_or_404(Movie, id=id)
        movie_del.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        