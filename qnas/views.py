from django.shortcuts import get_object_or_404, render, get_object_or_404 
from django.views.generic import ListView 
from qnas.models import Qna 

# Create your views here.
class QnaListView(ListView):
    model = Qna 
    template_name = 'qnas/qna_list.html'
    paginate_by = 7 
    context_object_name = 'qnas'
    ordering = ['-create_at']

def qna_detail(request, qna_id):
    qna = get_object_or_404(Qna, pk=qna_id)
    return render(request, 'qnas/qna_detail.html', {'qna': qna})
