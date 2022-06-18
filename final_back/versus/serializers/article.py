from rest_framework import serializers
from ..models import Article, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'user_photo')


class ArticleListSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)


class ArticleSerializer(serializers.ModelSerializer):

    class CommentSerializer(serializers.ModelSerializer):
        
        user = UserSerializer(read_only=True)

        class Meta:
            model = Comment
            fields = ('id', 'user', 'versus_vote', 'versus_content', 'article')

    comment_set = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)