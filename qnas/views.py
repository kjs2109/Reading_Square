from django.shortcuts import get_object_or_404, render, get_object_or_404, redirect 
from django.views.generic import ListView
from qnas.models import Qna, Answer 
from qnas.forms import AnswerForm, QnaForm 

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

def answer_delete(request, qna_id, answer_id):
    if request.user.is_authenticated:
        answer = get_object_or_404(Answer, pk=answer_id)
        answer.delete() 
        return redirect('qnas:qna_detail', qna_id=qna_id)
    else:
        return render(request, 'users/login_required.html')

def qna_create(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = QnaForm() 

        elif request.method == 'POST':
            form = QnaForm(request.POST)
            if form.is_valid():
                new_qna = form.save(commit=False)
                new_qna.user = request.user
                new_qna.save()
                return redirect('qnas:qna_detail', qna_id=new_qna.id)

        return render(request, 'qnas/qna_form.html', {'form': form})
    
    else:
        return render(request, 'users/login_required.html')

def qna_update(request, qna_id):
    if request.user.is_authenticated:
        qna = get_object_or_404(Qna, pk=qna_id)

        if request.user != qna.user:
            return redirect('qnas:qna_detail', qna_id=qna_id)

        if request.method == 'GET':
            form = QnaForm(instance=qna)

        elif request.method == 'POST':
            form = QnaForm(request.POST)
            if form.is_valid():
                qna.title = form.cleaned_data['title']
                qna.content = form.cleaned_data['content']
                qna.content_type = form.cleaned_data['content_type']
                qna.save()
                return redirect('qnas:qna_detail', qna_id=qna_id)
        return render(request, 'qnas/qna_form.html', {'form': form})

    else:
        return render(request, 'users/login_required.html')
