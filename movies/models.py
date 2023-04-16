from django.db import models

class RatingChoices(models.TextChoices):
     G = 'G'
     PG = 'PG'
     PG_13 = 'PG-13'
     R = 'R'
     Nc_17 = 'NC-17'    

class Movie(models.Model):
     title = models.CharField(max_length=127)
     duration = models.CharField(max_length=10, blank=True, null=True)
     rating = models.CharField(max_length=10, choices=RatingChoices.choices, default=RatingChoices.G)
     synopsis  = models.TextField(null=True, blank=True)
     user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="movies", null=True)

class OrderMovie(models.Model):
     user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="order_movies")
     movies = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="order_movies")
     buyed_at = models.DateTimeField(auto_now_add=True)
     price = models.DecimalField(max_digits=8, decimal_places=2)
     
     def __repr__(self) -> str:
          return f"<OrderMovie [{self.id}] - {self. price}"
