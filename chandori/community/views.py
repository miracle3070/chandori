from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog

def board(request):
    return render(request, "board.html")

def community(request):
    # Comm = request.GET[""]
    return render(request, "comm_main.html")

def write(request):
    return render(request, "create_content.html")

def create(request):
    if(request.method == 'POST'):
        new_blog = Blog()
        new_blog.title = request.POST['title']
        new_blog.writer = request.POST['writer']
        new_blog.body = request.POST['body']
        new_blog.pub_date = timezone.now()
        # new_blog.save()
    return redirect('community')
    # return render(request, 'create_content.html')

def detail(request):
    return render(request, "detail.html")

def detail_ques(request):
    return render(request, "detail_ques.html")

def inform(request):
    return render(request, "inform.html")

def question(request):
    return render(request, "question.html")

def delete(request, id):
    blog = get_object_or_404(Blog, pk=id)
    blog.delete()

    return redirect('community')

# def good(request){
#     blog = get_object_or_404(blog)
# }