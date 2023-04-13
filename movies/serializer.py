from rest_framework import serializers
from .models import OrderMovie, Movie, RatingChoices

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.Charfield(max_length=10, default=None)
    rating = serializers.ChoiceField(choices=RatingChoices.choices, default=RatingChoices.G)
    synopsis = serializers.CharField(default=None)
    added_by = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True) 



    def get_added_by(self, obj):
        return obj.user.email 
