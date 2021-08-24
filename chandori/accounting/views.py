from django.shortcuts import render, redirect

def home(request):
    return render(request, "base.html")

def field(request):
    return render(request, "account-field.html")