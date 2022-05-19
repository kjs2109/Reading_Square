from django.db.models import Q
from django import forms 
from posts.models import Post 
from my_rooms.models import Book

class PostForm(forms.ModelForm):

    class Meta:
        model = Post 
        fields = ['title', 'book', 'book_rating', 'content', 'link_title', 'link', 'publick'] 
        widgets = {
            'book_rating': forms.RadioSelect,
            'book': forms.Select(attrs={'class': 'select'}),  # choices를 사용하면 기본 폼으로 Select가 적용된다.
        }
    
    # 뷰에서 폼 객체를 생성할 때 현재 접속된 유저 정보를 넣어주기 위해 생성자 메소드를 오버라이딩 하였다.  
    # 입력 받은 유저 정보는 해당 유저의 책 정보만 가져오는데 사용된다.
    def __init__(self, user=None, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.filter(Q(user=user) & Q(used_post = False))