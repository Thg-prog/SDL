from django.shortcuts import render
from .models import Article

def index(request):
    articles=Article.objects.order_by('pub_date')
    return render(request,'article/index.html',{'title':'Главная страница','info':articles})


def about(request):
    articles=Article.objects.order_by('pub_date')
    return render(request,'article/about.html',{'title':'Главная страница','info':articles})
