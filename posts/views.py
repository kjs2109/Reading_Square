from django.shortcuts import render
from django.views.generic import ListView 
from posts.models import Post

# Create your views here.
class PostListView(ListView):
    model = Post 
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'
    paginate_by = 9 
    ordering = ['-create_at']

