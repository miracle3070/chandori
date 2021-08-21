from django.shortcuts import render, redirect

def board(request):
    return render(request, "templates/board_info.html")