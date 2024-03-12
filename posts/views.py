from django.shortcuts import render
from . models import Post
# Create your views here.
def index(request):
    posts = Post.objects.order_by('created_at') #get the latest post at the top of the page
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    post = Post.objects.get(id = pk)
    return render(request, 'post.html', {'post': post})