from rest_framework import serializers
from .models import Movie, RatingChoices
from .models import MovieOrder

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField(choices=RatingChoices.choices, default=RatingChoices.G)
    synopsis = serializers.CharField(default=None)
    added_by = serializers.SerializerMethodField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True) 
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return Movie.objects.create(**validated_data)


    def get_added_by(self, obj):
      
        return obj.user.email 
        
class OrderMovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True, source='movies.title')
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)


    
    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
  
    def to_representation(self, instance):
        new_objt = {
            'id': instance.id,
            'title': instance.movies.title,
            'buyed_at': instance.buyed_at,
            'price': format(instance.price, '.2f'),
            'buyed_by': instance.user.email
        }
        return new_objt