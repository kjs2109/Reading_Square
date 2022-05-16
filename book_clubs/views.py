from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.views.generic import ListView 
from .models import BookClub, ClubPost, Comment 
from users.models import User
from book_clubs.forms import CommentForm, ClubForm

# Create your views here.
class ClubListView(ListView):
    model = BookClub
    template_name = 'book_clubs/book_club_list.html'
    context_object_name = 'clubs' 
    paginate_by = 5
    ordering = ['-create_at']

def club_detail(request, club_id):
    if request.user.is_authenticated:
        # 해당 book_club에 속하는 포스트와 댓글을 모두 db에서 가져온다.
        club = get_object_or_404(BookClub, pk=club_id)
        user = get_object_or_404(User, pk=request.user.id) 
        club_posts = ClubPost.objects.filter(club=club)
        club_post_comment = Comment.objects.filter(club=club)

        # 해당 모임의 member이면 GET으로 member가 아니면 POST로 요청이 온다.
        if request.method == 'GET':
            comment_form = CommentForm() 

        elif request.method == 'POST':  # book_club에 참여하는 로직 
            # ManyToMany 관계에서 추가는 add() 삭제는 remove() 사용. db에 저장까지 된다.
            if user in club.members.all():
                club.memebers.remove(request.user)
                return redirect('clubs:club_list')
            
            else:
                club.members.add(request.user) 
                comment_form = CommentForm() 
        
        return render(
            request,
            'book_clubs/book_club_detail.html',
            {'club': club, 'club_posts': club_posts, 'comments': club_post_comment, 'comment_form': comment_form}
        )

    else:
        return render(request, 'book_clubs/login_required/login_required_enter.html')

def club_create(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)

        if request.method == 'GET':
            form = ClubForm(user=user) 

        elif request.method == 'POST':
            form = ClubForm(user, request.POST)
            if form.is_valid():
                new_club = form.save(commit=False)
                new_club.host = request.user 
                new_club.save() 
                return redirect('clubs:club_list') 
            
        return render(request, 'book_clubs/create_book_club_form.html', {'form': form})
        
    else:
        return render(request, 'book_clubs/login_required/login_required_create.html')