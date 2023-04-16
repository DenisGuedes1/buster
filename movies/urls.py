from django.urls import path
from .views import MovieView, OrderByMovie, OtherMovieIdView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:id>/", OtherMovieIdView.as_view()),
    path("movies/<int:movie_id>/orders/", OrderByMovie.as_view())
]