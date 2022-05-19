from django.db import models
from home.models import TimeStampedModel
from users.models import User
from my_rooms.models import Book

# Create your models here.
class Post(TimeStampedModel):

    RATING_CHOICES = (
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    )

    title = models.CharField(max_length=50)
    book_rating = models.IntegerField(choices=RATING_CHOICES, default=None)
    content = models.TextField()
    link_title = models.CharField(max_length=30, default='링크 제목')
    link = models.URLField(blank=True)
    publick = models.BooleanField(default=True)
    
    book = models.ForeignKey(Book, related_name='posts', on_delete=models.CASCADE)  # Null로 바뀐 다면 원래 Book을 참조하던 값들은 어떻게 되는 것인가..
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
