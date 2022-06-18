from django.db import models
from django.conf import settings

# Create your models here.

class Weather(models.Model):
    weather_status = models.CharField(max_length=50)


class Genre(models.Model):
    genre = models.CharField(max_length=50)
    weather_genre = models.ManyToManyField(Weather, related_name="genres")


class Actor(models.Model):
    name = models.CharField(max_length=50)
    poster_url = models.TextField(null=True)



class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    poster_url = models.TextField()
    director = models.CharField(max_length=30)
    director_poster = models.TextField(null=True)
    actors = models.ManyToManyField(Actor,related_name='movies')
    rating = models.FloatField(max_length=10,null=True)
    release_date = models.DateTimeField(null = True)
    genre = models.ManyToManyField(Genre, related_name='movies')
    movie_id = models.IntegerField()




class Review(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    user_rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Youtube(models.Model):
    youtube_link = models.TextField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    youtube_thumbnail = models.TextField()