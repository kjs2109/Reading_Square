from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView  
from posts.models import Post
from posts.forms import PostForm, PostUpdateForm

# Create your views here.
# class PostListView(ListView):
#     model = Post 
#     template_name = 'posts/posts_list.html'
    # context_object_name = 'posts'
    # paginate_by = 9 
    # ordering = ['-create_at']

    # 비공개 포스트는 제외하고 페이지 네이션 적용
def post_list(request):
    publick_posts =  Post.objects.filter(publick=True).order_by('-create_at')
    paginator = Paginator(publick_posts, 9)
    curr_page_number = request.GET.get('page')
    if curr_page_number is None:
        curr_page_number = 1 
    page = paginator.page(curr_page_number)
    return render(request, 'posts/post_list.html', {'page': page})

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
                new_post.book.used_post = True 
                new_post.save() 
                new_post.book.save()
                return redirect('posts:post_detail', post_id=new_post.id)

        return render(request, 'posts/post_form.html', {'form': form})
        
    else:
        return redirect('login_required')

# class PostUpdateView(UpdateView):
#     model = Post 
#     form_class = PostForm 
#     template_name = 'posts/post_form.html'
#     pk_url_kwarg = 'post_id' 

#     def get_form(self, form_class=None):
#         form_class = PostForm(user=self.request.user)
#         return form_class

#     def get_success_url(self):
#         return reverse('posts:post_detail', kwargs={'post_id', self.object.id})

def post_update(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)

        if request.user != post.author:
            return redirect('posts:post_detail', post_id=post_id)

        if request.method == 'GET':
            form = PostUpdateForm(instance=post)
        
        elif request.method == 'POST':
            form = PostUpdateForm(request.POST) 
            if form.is_valid():
                post.title = form.cleaned_data['title']
                post.content = form.cleaned_data['content']
                post.book_rating = form.cleaned_data['book_rating']
                post.publick = form.cleaned_data['publick']
                post.save() 
                return redirect('posts:post_detail', post_id=post_id)  
        return render(request, 'posts/post_update_form.html', {'form': form, 'post': post})

    else:
        return redirect('login_required')


def post_delete(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)
        if request.user != post.author:
            return redirect('posts:posts') 

        if request.method == 'GET':
            return render(request, 'posts/post_confirm_delete.html', {'post': post})

        elif request.method == 'POST':
            post.book.used_post = False 
            post.book.save()
            post.delete() 
            return redirect('posts:posts')
    
    else:
        return redirect('login_required')
