from django.shortcuts import render
from django.urls import reverse 
from allauth.account.views import PasswordChangeView

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

class CustomPasswordChangeView(PasswordChangeView):  # PasswordChageView 대신 CustomPasswordChangeView를 사용하도록 url 패턴도 바꿔줘야함
    def get_success_url(self):
        return reverse('home:home')
