from django.urls import path
from .views import MovieView, OrderByMovie, OtherMovieIdView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:id>/", OtherMovieIdView.as_view()),
    path("movies/order/<int:movie_id>/", OrderByMovie.as_view())
]