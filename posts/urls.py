from django.urls import path 
from . import views 

app_name = 'posts'
urlpatterns = [
    # posts 
    path('', views.PostListView.as_view(), name='posts'),
    # posts/1/detail/ 
    path('<int:post_id>/detail/', views.PostDetailView.as_view(), name='post_detail'),
    # posts/create/ 
    # path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('create/', views.post_create, name='post_create'),
    # posts/1/update/ 
    # path('<int:post_id>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:post_id>/update/', views.post_update, name='post_update'),
    # posts/1/delete/ 
]