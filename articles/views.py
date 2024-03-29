from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.

# Read 함수
def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles
    }
    
    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    
    context = {
        'article': article
    }
    
    return render(request, 'detail.html', context)

# Create 함수
def create(request):
    if request.method == 'POST':
        form =ArticleForm(request.POST)
        if form.is_valid():
            article=form.save()
            return redirect('articles:detail', id=article.id)
        
    else:
        form = ArticleForm()
            
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)

# Delete 함수
def delete(request):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles:index')

# Update 함수
def update(request, id):
    article = Article.objects.get(id=id)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        
        if form.is_valid():
            form.save()
            return redirect('articles:detail', id=id)
        
    else:
        form =ArticleForm(instance=article)
        
    context = {
        'form': form,
    }
    
    return render(request, 'update.html', context)