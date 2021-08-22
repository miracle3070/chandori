from django.shortcuts import render, redirect

def community(request):
    return render(request, "board.html")