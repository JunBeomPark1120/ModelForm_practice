from django.shortcuts import render
from .models import Article

# Create your views here.

# Read 함수
def index(request):
    article = Article.objects.all()
    
    context = {
        'article': article
    }
    
    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    
    context = {
        'article': article
    }
    
    return render(request, 'detail.html', context)