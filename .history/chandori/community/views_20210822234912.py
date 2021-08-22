from django.shortcuts import render, redirect

def community(request):
    return render(request, "board_info.html")