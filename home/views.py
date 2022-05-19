import random
from django.shortcuts import render
from django.urls import reverse 
from django.views.generic import ListView 
from allauth.account.views import PasswordChangeView
from book_clubs.models import BookClub
from home.models import BookVerse 

# Create your views here.
class HomeClubListView(ListView):
    model = BookClub
    template_name = 'home/home.html'
    context_object_name = 'clubs' 
    paginate_by = 5
    ordering = ['-create_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rand_id = random.randint(1, BookVerse.objects.all().count())
        context['verse'] = BookVerse.objects.get(id=rand_id)
        return context 

def intro(reqeust):
    return render(reqeust, 'home/intro.html')

class CustomPasswordChangeView(PasswordChangeView):  # PasswordChageView 대신 CustomPasswordChangeView를 사용하도록 url 패턴도 바꿔줘야함
    def get_success_url(self):
        return reverse('home:home')
