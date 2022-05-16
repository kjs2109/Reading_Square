from django.db import models
from home.models import TimeStampedModel
from users.models import User 

# Create your models here.
class Book(TimeStampedModel):

    STATUS_CHOICES = (
        (1, '읽기 전'),
        (2, '읽는 중'),
        (3, '읽은 후'),
    )

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    memo = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    book_image = models.ImageField(upload_to='book_pics/', default='default_book_cover.png')

    used_club = models.BooleanField(default=False)
    used_post = models.BooleanField(default=False)

    user = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title 
