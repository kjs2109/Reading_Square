from django.urls import path 
from . import views 

app_name = 'posts'
urlpatterns = [
    # posts 
    path('', views.PostListView.as_view(), name='posts'),
    # posts/1/detail/ 

    # posts/create/ 

    # posts/1/update/ 

    # posts/1/delete/ 
]