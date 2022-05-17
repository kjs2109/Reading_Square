from django.urls import path 
from . import views 

app_name = 'users'
urlpatterns = [
    # users/1/profile/
    path('<int:user_id>/profile/', views.profile, name='profile'),
]