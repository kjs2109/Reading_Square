from django import forms
from qnas.models import Qna 

class QnaForm(forms.ModelForm):
    class Meta:
        model = Qna 
        fields = ['title', 'content', 'content_type']