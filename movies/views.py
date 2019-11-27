from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import GenreSerializer, MovieSerializer, GradeSerializer, DirectorSerializer, ReviewSerializer, MovieDetailSerializer, TempReviewSerializer, MovieReviewSerializer
from .models import Genre, Movie, Review, Director, Grade
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny, ])
def grades(request):
    grades = Grade.objects.all()
    serializer = GradeSerializer(grades, many=True)
    return Response(serializer.data)
    # return JsonResponse(serializer.data, safe=False)



@api_view(['GET'])
@permission_classes([AllowAny, ])
def directors(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(serializer.data)
    # return JsonResponse(serializer.data, safe=False)



@api_view(['GET'])
@permission_classes([AllowAny, ])
def genres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)
    # return JsonResponse(serializer.data, safe=False)



@api_view(['GET'])
@permission_classes([AllowAny, ])
def movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
    # return JsonResponse(serializer.data, safe=False)



@api_view(['GET'])
@permission_classes([AllowAny, ])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)






# @api_view(['GET'])
# @permission_classes([AllowAny, ])
# def reviews(request):
#     reviews = Review.objects.all()
#     serializer = TempReviewSerializer(reviews, many=True)
#     return Response(serializer.data)
    # return JsonResponse(serializer.data, safe=False)



@api_view(['POST'])
@permission_classes([IsAuthenticated,])  
@authentication_classes([JSONWebTokenAuthentication,])  
def create_reviews(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, review_user=request.user)
        # return Response({'message':"작성되었습니다."})
        return JsonResponse(serializer.data)
    return HttpResponse(status=400)


@api_view(['PUT', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated,]) 
@authentication_classes([JSONWebTokenAuthentication,])
def reviews_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    serializer = ReviewSerializer(data=request.data)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)
        return HttpResponse(status=400)
    elif request.method == 'DELETE':
        review.delete()
        return Response({'message':"삭제되었습니다."})




@api_view(['GET'])
@permission_classes([AllowAny, ])
def movie_reviews(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.review_set.all()
    serializer = MovieReviewSerializer(reviews, many=True)
    return Response(serializer.data)
    # return JsonResponse(serializer.data, safe=False)




















# @api_view(['POST'])
# @permission_classes([IsAuthenticated, ])
# @authentication_classes([JSONWebTokenAuthentication, ])
# def post_create(request):
#     movie = get_object_or_404(Movie, id=request.data.get('movie_id'))
#     post = PostCreateSerializer(data=request.data)
#     if post.is_valid(raise_exception=True):
#         post = post.save(movie_id=movie.id, user=request.user)

#         content = request.data.get('content').split(' ')
#         hashtag_create(post, content)

#         serializer = PostSerializer(instance=post)
#         return JsonResponse(serializer.data)
#     return HttpResponse(status=400)


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([AllowAny, ])
# def post_detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return JsonResponse(serializer.data)
#     else:
#         if request.user == post.user:
#             if request.method == 'PUT':
#                 serializer = PostCreateSerializer(
#                     instance=post, data=request.data)
#                 if serializer.is_valid(raise_exception=True):
#                     post = serializer.save(
#                         movie_id=request.data.get('movie_id'), user=request.user)

#                     for hashtag in post.hashtags.all():
#                         post.hashtags.remove(hashtag)

#                     content = request.data.get('content').split(' ')
#                     hashtag_create(post, content)

#                     serializer = PostSerializer(post)
#                     return JsonResponse(serializer.data)
#             else:
#                 post.delete()
#                 return JsonResponse({'message': '삭제가 완료되었습니다.'})
#     return HttpResponse('잘못된 요청입니다.', status=403)