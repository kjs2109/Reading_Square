from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(
        max_length=15, 
        unique=True, 
        null=True,
        error_messages={'unique': '이미 사용중인 닉네임 입니다.'},
        validators = [validate_no_special_characters],
    )
        
    fav_verse = models.TextField(blank=True)
    bio = models.CharField(max_length=255, blank=True)
    profile_photo = models.ImageField(upload_to='profile_pics/', default='default_profile_pic.jpg')
    benner_image = models.ImageField(upload_to='benner_imgs/', default='bg1.jpg')

    def __str__(self):
        if self.nickname:
            return self.nickname
        else:
            return self.username