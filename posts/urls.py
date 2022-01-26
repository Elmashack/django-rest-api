from django.urls import path

from .views import PostListAPI, PostDetailAPI, UserListAPI, UserDetailAPI


urlpatterns = [
    path('users/', UserListAPI.as_view()),
    path('users/<int:pk>/', UserDetailAPI.as_view()),
    path('<int:pk>/', PostDetailAPI.as_view()),
    path('', PostListAPI.as_view()),
]


