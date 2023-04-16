from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, Request, status

from .models import Movie
from .serializer import MovieSerializer, OrderMovieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import(
    IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly)
from users.permission import IsAdminOrReadOnly, IsAdminWithReadAccess
from movies.permission import AuthenticateUser, IsEmployee
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
class OrderByMovie(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AuthenticateUser]
    def post(self, request: Request, movie_id=int):
        movie = get_object_or_404(Movie, id=movie_id)
        serializers = OrderMovieSerializer(data=request.data)
        if serializers.is_valid():
            order = serializers.save(user=request.user, movies=movie)
            return Response(OrderMovieSerializer(order).data, status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)