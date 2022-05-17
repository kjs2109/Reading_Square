from django.shortcuts import render
from django.urls import reverse 
from django.views.generic import ListView 
from allauth.account.views import PasswordChangeView
from book_clubs.models import BookClub

# Create your views here.
class HomeClubListView(ListView):
    model = BookClub
    template_name = 'home/home.html'
    context_object_name = 'clubs' 
    paginate_by = 5
    ordering = ['-create_at']

# def home(request):
#     return render(request, 'home/home.html')

class CustomPasswordChangeView(PasswordChangeView):  # PasswordChageView 대신 CustomPasswordChangeView를 사용하도록 url 패턴도 바꿔줘야함
    def get_success_url(self):
        return reverse('home:home')
