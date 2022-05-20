from django import forms
from qnas.models import Qna, Answer  

class QnaForm(forms.ModelForm):
    class Meta:
        model = Qna 
        fields = ['title', 'content', 'content_type']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content'] 