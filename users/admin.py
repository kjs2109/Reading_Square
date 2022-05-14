from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User 

# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            'Customfields', {'fields': ('nickname', 'fav_verse', 'bio', 'profile_photo', 'benner_image',)}
        ),
    ) 
