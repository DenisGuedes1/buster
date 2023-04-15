from django.urls import path
from .views import MovieView, OtherMovieIdView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:id>", OtherMovieIdView.as_view())
]