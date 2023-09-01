from django.contrib.auth import get_user_model # for users
from rest_framework import generics
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer



class PostList(generics.ListCreateAPIView): # Lists all posts
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView): # Retrieves individual post
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView): # Lists all users
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView): # Retrieves individual user
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer