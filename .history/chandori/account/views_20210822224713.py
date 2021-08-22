from django.shortcuts import render, redirect

def edit(request):
    return render(request, "edit.html")