from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.

def index(request):
  all_posts = Post.objects.all()

  return render(request, 'blog/index.html', {
    'all_posts': all_posts
  })

def new(request):
  form = PostForm()

  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
       content = form.save()
    return redirect('post-detail', content.pk)

  context = {'form':form}
  return render(request, 'blog/new.html', context)


def post_detail(request,id):
  identified_post = Post.objects.get(id=id)
  return render (request, 'blog/post-detail.html', {
    "post": identified_post
  }) 


def edit(request, id):
    identified_post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=identified_post)
    return render(request, 'blog/edit.html', {
      'blog_post':identified_post,
      'form': form
    })

def update(request, id):
  if request.method == 'POST':
    identified_post = Post.objects.get(id=id)
    identified_post.title = request.POST.get('title')
    identified_post.content = request.POST.get('content')
    identified_post.save()
    return redirect('post-detail', id)

def delete(request, id):
  identified_post = Post.objects.get(id=id)
  identified_post.delete()
  return redirect('blog')
 