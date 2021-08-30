from django.db import models
from django.db.models.base import Model
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import BlogForm
from django.core.paginator import Paginator

def board(request):
    return render(request, "board.html")

# Create your views here.
def community(request):
    # Comm = request.GET[""]
    return render(request, "comm_main.html")

def write(request):
    form = BlogForm()
    return render(request, "create_content.html", {'form':form})

def create(request):
    form = BlogForm(request.POST)

    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.writer = request.user
        new_blog.save()

        if new_blog.category == "정보 게시판":
            return redirect('community:detail', new_blog.id)
        else:
            return redirect('community:detail_ques', new_blog.id)

    # if request.method == 'POST':
    #     new_blog = Blog()
    #     new_blog.title = request.POST['title']
    #     new_blog.writer = request.POST['writer']
    #     new_blog.body = request.POST['body']
    #     new_blog.pub_date = timezone.now()
    #     new_blog.save()
    return redirect('community:community')

def update(request, id):
    blog = get_object_or_404(Blog, pk=id)

    return render(request, "update.html", {'blog':blog})

def updateAction(request, id) :
    blog = get_object_or_404(Blog, pk=id)
    blog.title = request.POST['title']
    # blog.writer = request.POST['writer']
    # blog.category = request.POST['category']
    blog.content = request.POST['content']
    blog.save()

    if blog.category == "정보 게시판":    
        return redirect('community:detail', blog.id)
    else:
        return redirect('community:detail_ques', blog.id)

def delete(request, id):
    blog = get_object_or_404(Blog, pk=id)
    blog.delete()

    return redirect('community:community')

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)

    return render(request, "detail.html", {'blog':blog})

def detail_ques(request, id):
    blog = get_object_or_404(Blog, pk=id)

    return render(request, "detail_ques.html", {'blog':blog})

def inform(request):
    blog = Blog.objects.filter(category='정보 게시판').order_by('-created_date')
    return render(request, "inform.html", {"blogs":blog})

def question(request):
    blog = Blog.objects.filter(category='질문 게시판').order_by('-created_date')
    return render(request, "question.html", {'blogs':blog})

def my_content(request):
    blog = Blog.objects.filter(writer=request.user)
    return render(request, "my_content.html", {'blogs':blog})