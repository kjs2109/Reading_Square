from django.shortcuts import get_object_or_404, render, get_object_or_404 
from django.views.generic import ListView 
from qnas.models import Qna 
from qnas.forms import AnswerForm 

# Create your views here.
class QnaListView(ListView):
    model = Qna 
    template_name = 'qnas/qna_list.html'
    paginate_by = 7 
    context_object_name = 'qnas'
    ordering = ['-create_at']

def qna_detail(request, qna_id):
    qna = get_object_or_404(Qna, pk=qna_id)

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = AnswerForm(request.POST)
            if form.is_valid():
                new_answer = form.save(commit=False)
                new_answer.author = request.user 
                new_answer.question = qna 
                new_answer.save() 
        else:
            return render(request, 'users/login_required.html')

    answer_form = AnswerForm()
 
    return render(request, 'qnas/qna_detail.html', {'qna': qna, 'form': answer_form})
