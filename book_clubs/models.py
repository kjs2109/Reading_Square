from django.db import models
from posts.models import TimeStempedModel 
from users.models import User 
from my_rooms.models import Book

# Create your models here.
class BookClub(TimeStempedModel):
    name = models.CharField(max_length=50)
    intro = models.TextField(blank=True)
    rule = models.TextField(blank=True) 

    host = models.ForeignKey(User, related_name='book_clubs', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='clubs', on_delete=models.CASCADE)

    members = models.ManyToManyField(User, related_name='member_clubs', blank=True) 

class ClubPost(TimeStempedModel):
    title = models.CharField(max_length=50)
    content = models.TextField() 

    club = models.ForeignKey(BookClub, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='club_posts', on_delete=models.CASCADE)

class Comment(TimeStempedModel):
    content = models.TextField()

    club = models.ForeignKey(BookClub, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(ClubPost, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

