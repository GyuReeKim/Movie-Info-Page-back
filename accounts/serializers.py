from rest_framework import serializers
from .models import User
from movies.models import Movie, Review
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'like_genres', 'is_staff',)

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'poster_url',)

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = Review
        fields = ('movie', 'comment', 'score', 'create_at',)

class UserReviewSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True)
    class Meta:
        model = User
        fields = ('username', 'review_set',)