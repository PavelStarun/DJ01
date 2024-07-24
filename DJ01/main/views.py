from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def new(request):
    return HttpResponse("<h4>Это второя страница на моем новом сайте созданного с помощью Django</h4>")