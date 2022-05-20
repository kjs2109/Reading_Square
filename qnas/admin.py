from django.contrib import admin
from qnas.models import Qna

# Register your models here.
@admin.register(Qna)
class QnaAdmin(admin.ModelAdmin):
    pass 


