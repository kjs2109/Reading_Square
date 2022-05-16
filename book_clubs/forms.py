from django import forms 
from .models import Comment, BookClub
from my_rooms.models import Book

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['content']

# 유저 별로 맞춤형으로 폼을 만들수 있도록 user 정보를 추가로 입력 받는다.
class ClubForm(forms.ModelForm):
    class Meta: 
        model =  BookClub
        fields = ['name', 'intro', 'rule', 'book'] 

    def __init__(self, user=None, *args, **kwargs):
        super(ClubForm, self).__init__(*args, **kwargs) 
        self.fields['book'].queryset = Book.objects.filter(user=user)