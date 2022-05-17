from django import forms 
from .models import User 

# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = User 
#         fields = ['nickname']  # nickname 필드를 추가로 입력받는다.

#     def signup(self, request, user):
#         user.nickname = self.cleaned_data['nickname']  # form에서 입력받은 데이터는 cleaned_data에 저장된다.
#         user.save()  # form에서 입력 받은 nicname 데이터를 직접 user 테이블에 저장한다.

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['nickname', 'bio', 'fav_verse',  'profile_photo', 'benner_image']
        widgets = {
            'bio': forms.Textarea,
            'fav_verse': forms.Textarea,
        }