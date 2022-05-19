from django.contrib import admin
from home.models import BookVerse 

# Register your models here.
@admin.register(BookVerse)
class BookVerseModel(admin.ModelAdmin):
    pass 
