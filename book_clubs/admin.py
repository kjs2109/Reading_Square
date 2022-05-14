from django.contrib import admin
from .models import BookClub, ClubPost, Comment

# Register your models here.
@admin.register(BookClub)
class BookClubAdmin(admin.ModelAdmin):
    pass 

@admin.register(ClubPost)
class ClubPostAdmin(admin.ModelAdmin):
    pass 

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass 