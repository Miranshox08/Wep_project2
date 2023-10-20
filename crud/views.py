from django.shortcuts import render, redirect
from crud.models import Article
from crud.forms import ArticleFrom
# Create your views here.

def article_func(request):
    articles = Article.objects.all()
    return render(request, 'articles_list.html', {'articles': articles})

def article_detail(request, slug):
    article_detail = Article.objects.get(slug=slug)
    return render(request, 'articil_d')

def article_create(request):
    form = ArticleFrom(request.POST or None, request.FILES)
    if request.method == "POST" and form.is_valid():
        intance = form.save(commit=False)
        intance = author = request.user 
        intance.save()
        return redirect("article_func")
    form = ArticleFrom()
    return render(request, "article_create.html", {"form":form})

def article_edit(reuqest, slug):
    article = Article.objects.get(slug=slug)
    form = ArticleFrom(reuqest.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('article_detail', slug=reuqest.POST.get("slug"))
    return render(reuqest, 'article_edit,html', {"form": form, 'article': article})