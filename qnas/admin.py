from django.contrib import admin
from qnas.models import Qna, Answer

# Register your models here.
@admin.register(Qna)
class QnaAdmin(admin.ModelAdmin):
    pass 

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
