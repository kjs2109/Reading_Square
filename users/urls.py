from django.urls import path 
from . import views 

app_name = 'users'
urlpatterns = [
    # users/1/profile/
    path('<int:user_id>/profile/', views.profile, name='profile'),
    # users/1/post_list/
    path('<int:user_id>/post_list/', views.post_list, name='user_post_list'),
]