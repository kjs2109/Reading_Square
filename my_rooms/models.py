from django.db import models
from posts.models import TimeStempedModel
from users.models import User 

# Create your models here.
class Book(TimeStempedModel):

    STATUS_CHOICES = (
        (1, '읽기 전'),
        (2, '읽는 중'),
        (3, '읽은 후'),
    )

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    memo = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    book_image = models.ImageField(blank=True)

    user = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title 
