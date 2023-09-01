from django.urls import path
from .views import PostList, PostDetail, UserDetail, UserList

app_name = 'posts'

urlpatterns = [
    # Lists all users
    path('users/', UserList.as_view()),

    # Retrieves individual user
    path('users/<int:pk>/', UserDetail.as_view()),

    # Retrieves individual post
    path('<int:pk>/', PostDetail.as_view()),

    # Lists all posts
    path('', PostList.as_view()),
]