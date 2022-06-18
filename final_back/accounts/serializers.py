from rest_framework import serializers
from django.contrib.auth import get_user_model
from versus.models import Article, Comment
from movies.models import Movie, Review
from versus.serializers.article import ArticleSerializer

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id', 'title')

    class CommentSerializer(serializers.ModelSerializer):

        class Meta:
            model = Comment
            fields = ('id', 'article', 'versus_content',)

    class ReviewSerializer(serializers.ModelSerializer):
        
        class MovieSerializer(serializers.ModelSerializer):
            class Meta:
                model = Movie
                fields = ('movie_id', 'title')

        movie = MovieSerializer(read_only=True)

        class Meta:
            model = Review
            fields = ('id', 'title', 'movie', 'user_rate',)
        

    review_set = ReviewSerializer(many=True, read_only=True)
    article_set = ArticleSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', 'review_set', 'article_set', 'comment_set', 'user_photo', 'about')
