from django.shortcuts import render
from .models import Article

# Create your views here.
def articles(request):
    articles = Article.objects.all()
    context: dict = {
        "articles": articles
    }
    return render(request, "articles/index.html", context = context)