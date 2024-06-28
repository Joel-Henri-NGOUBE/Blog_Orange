from django.shortcuts import render, redirect
from .models import Article, User
from django.utils.translation import gettext
from django.views import View

# Create your views here.
def articles(request):
    bonjour = gettext("bonjour")
    articles = Article.objects.all()
    context: dict = {
        "articles": articles
    }
    return render(request, "articles/index.html", context = context)

# @http_method_list(["GET","POST"])
class Login(View):
    def get(self, request):
        return render(request, "login/index.html")
    
    def post(self, request):
        mail, password = request.POST.dict().values
        message = {}
        if mail and password:
            user = User.objects.filter(mail=mail)
            print(user)
            if(len(user)):
                if password == "":
                    # Redirection
                    redirect("/blog")
                else:
                    message["error"] = "Mot de passe incorrect"
                    return render(request, "login/index.html", context = message) 
            else:
                message["error"] = "Utilisateur introuvable"
                return render(request, "login/index.html", context = message) 
        message["error"]  = "Un ou plusieurs champs non renseignés"
        return render(request, "login/index.html", context = message)   
    
class Signup(View):
    def get(self, request):
        return render(request, "signup/index.html")
    
    def post(self, request):
        mail, username, password = request.POST.dict().values
        message = {}
        if mail and username and password:
            user = User.objects.filter(mail=mail)
            print(user)
            if(len(user)):
                message["error"] = "Adresse mail déjà utilisée"
                return render(request, "signup/index.html", context = message) 
            else:
                User.objects.create(
                email = mail,
                username = username,
                password = password
            )
                message["success"] = "Utilisateur créé avec succès"
                return render(request, "signup/index.html", context = message) 
        message["error"]  = "Un ou plusieurs champs non renseignés"
        return render(request, "signup/index.html", context = message)
    
        # print(request.body.decode())
        # print(list(request.POST.items()))
        # print(dict(request.POST.items())) 