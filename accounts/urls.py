from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users),
    path('signup/', views.signup),
    path('<int:id>/', views.detail),
]