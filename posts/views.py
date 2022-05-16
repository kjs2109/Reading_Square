from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView  
from posts.models import Post
from posts.forms import PostForm

# Create your views here.
class PostListView(ListView):
    model = Post 
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'
    paginate_by = 9 
    ordering = ['-create_at']

class PostDetailView(DetailView):
    model = Post 
    template_name = 'posts/post_detail.html'
    pk_url_kwarg = 'post_id'

# class PostCreateView(CreateView):
#     model = Post 
#     template_name = 'posts/post_form_1.html'

#     def get_form(self, form_class=None):
#         form_class = PostForm(user=self.request.user)
#         return form_class

#     # form_valid는 폼의 입력받은 폼의 유효성을 검사하고 db에 저장하는 메소드다.
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form) # 여기서 super()는 PostCreateView의 상위 클래스인 CreateView를 의미한다.

#     def get_success_url(self):
#         return reverse('post_detail', kwargs={'post_id': self.object.id})

def post_create(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = PostForm(user=request.user) 

        elif request.method == 'POST':
            form = PostForm(request.user, request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.author = request.user 
                new_post.save() 
                return redirect('posts:post_detail', post_id=new_post.id)

        return render(request, 'posts/post_form.html', {'form': form})
        
    else:
        return redirect('account_login')


