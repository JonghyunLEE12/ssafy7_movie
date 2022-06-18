from asyncore import read
from rest_framework import serializers
from . models import (
    Weather,
    Genre,
    Movie,
    Actor,
    Review,
    Youtube,
    Review,
    
)
from django.contrib.auth import get_user_model

User = get_user_model()

class TodayWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather,
        fields = '__all__'

class WeatherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'

class RecommendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields ='title','poster_url','rating','description','release_date'

class ReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = User
            fields = ('id', 'username', 'user_photo',)
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)


class MovieDetailSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('genre',)

    genre = GenreSerializer(many=True, read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title','poster_url','rating','description','release_date', 'movie_id', 'review_set', 'genre')
