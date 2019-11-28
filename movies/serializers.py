from rest_framework import serializers
from .models import Genre, Movie, Review, Director, Grade
from accounts.models import User


class TempUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class TempGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name',)

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('id', 'name',)

class TempMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'title_en', 'score', 'audience', 'poster_url', 
        'summary', 'movie_directors', 'video_url', 'ost_url', 'movie_genres', 'grade',)


class DirectorSerializer(serializers.ModelSerializer):
    director_movies = TempMovieSerializer(many=True)
    # movie_genres = GradeSerializer(many=True)
    class Meta:
        model = Director
        fields = ('id', 'name', 'director_movies', )

class MovieSerializer(serializers.ModelSerializer):
    movie_genres = TempGenreSerializer(many=True)
    movie_directors = DirectorSerializer(many=True)
    grade = GradeSerializer()
    class Meta:
        model = Movie
        fields = ('id', 'title', 'title_en', 'score', 'audience', 'poster_url', 
        'summary', 'movie_directors', 'video_url', 'ost_url', 'movie_genres', 'grade',)

class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, source='genre_movies')
    # like_users = serializers.SlugRelatedField(many=True, read_only=True, slug_field='username')
    class Meta:
        model = Genre
        fields = ('id', 'name', 'movies')

class MovieDetailSerializer(serializers.ModelSerializer):
    movie_genres = GenreSerializer(many=True)
    movie_directors = DirectorSerializer(many=True)
    grade = GradeSerializer()
    class Meta:
        model = Movie
        fields = ('id', 'title', 'title_en', 'score', 'audience', 'poster_url',
         'summary', 'movie_directors', 'video_url', 'ost_url', 'movie_genres', 'grade',)


# delete, put, post
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('comment', 'score',)



class TempReviewSerializer(serializers.ModelSerializer):
    review_user = TempUserSerializer()
    # create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta:
        model = Review
        fields = ('id', 'comment', 'score', 'movie', 'review_user', 'create_at',)


# class TempReviewSerializer(serializers.ModelSerializer):
#     # review_user = TempUserSerializer()
#     class Meta:
#         model = Review
#         fields = ('comment', 'score',)


class MovieReviewSerializer(serializers.ModelSerializer):
    review_user = TempUserSerializer()
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta:
        model = Review
        fields = ('__all__')