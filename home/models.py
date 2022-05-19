from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True) 

    class Meta:
        abstract = True 

class BookVerse(TimeStampedModel):
    verse = models.TextField()
    verse_from = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.verse[:20]