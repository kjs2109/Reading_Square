from django.shortcuts import render
from django.views.generic import ListView 
from qnas.models import Qna 

# Create your views here.
class QnaListView(ListView):
    model = Qna 
    template_name = 'qnas/qna_list.html'
    paginate_by = 7 
    context_object_name = 'qnas'
    ordering = ['-create_at']
