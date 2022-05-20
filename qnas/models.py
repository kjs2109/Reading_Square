from django.db import models
from home.models import TimeStampedModel
from users.models import User 

# Create your models here.
class Qna(TimeStampedModel):

    TYPE_CHOICES = (
        ('기타', '기타'),
        ('건의 사항', '건의 사항'),
        ('오류 제보', '오류 제보'),
        ('질문', '질문'),
    )

    title = models.CharField(max_length=50)
    content = models.TextField()
    content_type = models.CharField(choices=TYPE_CHOICES, max_length=10)

    user = models.ForeignKey(User, related_name='qnas', on_delete=models.CASCADE)

    def __str__(self):
        return self.title 

class Answer(TimeStampedModel):
    content = models.TextField() 
    question = models.ForeignKey(Qna, related_name='answers', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)

    def __str__(self): 
        return self.content[:30]
