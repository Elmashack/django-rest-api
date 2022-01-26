from rest_framework import generics, permissions
from django.contrib.auth import get_user_model

from .permissions import IsAuthorReadOnly
from .serializer import PostSerializer, UserSerializer
from .models import PostClass


class PostListAPI(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated, )
    queryset = PostClass.objects.all()
    serializer_class = PostSerializer


class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.IsAuthenticated, IsAuthorReadOnly,)
    queryset = PostClass.objects.all()
    serializer_class = PostSerializer


class UserListAPI(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
