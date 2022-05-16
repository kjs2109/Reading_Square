from django.db.models import Q 
from django import forms 
from .models import Comment, BookClub, ClubPost
from my_rooms.models import Book

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['content']
        widgets = {
            'content': forms.TextInput,
        }

# 유저 별로 맞춤형으로 폼을 만들수 있도록 user 정보를 추가로 입력 받는다.
class ClubForm(forms.ModelForm):
    class Meta: 
        model =  BookClub
        fields = ['name', 'intro', 'rule', 'book'] 

    def __init__(self, user=None, *args, **kwargs):
        super(ClubForm, self).__init__(*args, **kwargs) 
        self.fields['book'].queryset = Book.objects.filter(Q(user=user) & Q(used_club=False))

class ClubPostForm(forms.ModelForm):
    class Meta:
        model = ClubPost 
        fields = ['title', 'content']