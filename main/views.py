from django.shortcuts import render
from .models import Article
from django.utils.translation import gettext

# Create your views here.
def articles(request):
    bonjour = gettext("bonjour")
    articles = Article.objects.all()
    context: dict = {
        "articles": articles
    }
    return render(request, "articles/index.html", context = context)