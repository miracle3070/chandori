from django.shortcuts import render, redirect

def board2(request):
    return render(request, "board_q.html")