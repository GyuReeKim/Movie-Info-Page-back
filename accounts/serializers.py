from rest_framework import serializers
from .models import User
from movies.models import Movie, Review, Genre

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'like_genres', 'is_staff',)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name',)


class MovieSerializer(serializers.ModelSerializer):
    movie_genres = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('title', 'poster_url', 'movie_genres')


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = Review
        fields = ('movie', 'comment', 'score', 'create_at', )

class UserReviewSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True)
    class Meta:
        model = User
        fields = ('username', 'review_set',)