from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import AuthenticationForm

from rest_framework.decorators import api_view, permission_classes

from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.settings import api_settings

from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserReviewSerializer

@api_view(['GET'])
@permission_classes([AllowAny, ])
def users(request):
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    # return Response(serializer.data)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        jwt_payload = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode = api_settings.JWT_ENCODE_HANDLER
        user = serializer.save()

        payload = jwt_payload(user)
        token = jwt_encode(payload)

        return JsonResponse({'token': token})
    return HttpResponse(status=400)


@api_view(['GET'])
@permission_classes([AllowAny, ])
def detail(request, id):
    user = get_object_or_404(get_user_model(), id=id)
    serializer = UserReviewSerializer(user)
    return JsonResponse(serializer.data)


# @api_view(['POST'])
# @permission_classes([AllowAny,])
# def signup(request):
#     serializer = UserSerializer(data=request.POST)
#     if serializer.is_valid(raise_exception=True):
#         password = serializer.validated_data.get('password')
#         user = serializer.save()
#         user.set_password(raw_password=password)
#         user.save()
        
#         return JsonResponse(serializer.data)
#     return HttpResponse(status=400)



# @api_view(['GET'])
# @permission_classes([IsAuthenticated, ])
# @authentication_classes([JSONWebTokenAuthentication, ])
# def user_detail(request, user_id):
#     user = get_object_or_404(get_user_model(), id=user_id)
#     if request.user == user:
#         serializer = UserSerializer(user)
#         return JsonResponse(serializer.data)
#     return HttpResponse('허가되지않은 접근입니다.', status=403)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated, ])
# @authentication_classes([JSONWebTokenAuthentication, ])
# def user_posts(request, user_id):
#     user = get_object_or_404(get_user_model(), id=user_id)
#     posts = user.posts.all()
#     serializer = PostSerializer(posts, many=True)
#     return JsonResponse(serializer.data, safe=False)