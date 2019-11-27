from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.genres),
    
    path('movies/', views.movies),
    path('<int:movie_id>/', views.movie_detail),

    # path('grades/', views.grades),
    path('directors/', views.directors),

    # path('reviews/', views.reviews),
    path('<int:movie_id>/reviews/', views.create_reviews),
    path('reviews/<int:review_id>/', views.reviews_detail),
    path('<int:movie_id>/reviewall/', views.movie_reviews),
    # path('<int:movie_id>/reviewswatch/', views.reviews_watch)
]