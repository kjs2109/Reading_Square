from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView 
from .models import BookClub

# Create your views here.
class ClubListView(ListView):
    model = BookClub
    template_name = 'book_clubs/book_club_list.html'
    context_object_name = 'clubs' 
    paginate_by = 5
    ordering = ['-create_at']

