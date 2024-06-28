from django.shortcuts import render, redirect, resolve_url
from .models import Article, User
from django.utils.translation import gettext
from django.views import View
from .utils.utils_functions import get_route_params

# Create your views here.
def articles(request):
    bonjour = gettext("bonjour")
    articles = Article.objects.all()
    context: dict = get_route_params("blog")
    context["articles"] = articles
    return render(request, "articles/index.html", context = context)

class Chat(View):
    def get(self, request):
        context: dict = get_route_params("chat")
        return render(request, "chat/index.html", context = context)
    def post(self, request):
        return render(request, "chat/index.html")
    
class NewPost(View):
    def get(self, request):
        context: dict = get_route_params("newpost")
        return render(request, "newpost/index.html", context = context)
    def post(self, request):
        return render(request, "newpost/index.html")

# @http_method_list(["GET","POST"])
class Login(View):
    def get(self, request):
        context: dict = get_route_params("login")
        return render(request, "login/index.html", context = context)
    
    def post(self, request):
        mail, password = request.POST.dict().values
        message: dict = get_route_params("login")
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
        context: dict = get_route_params("signup")
        return render(request, "signup/index.html", context = context)
    
    def post(self, request):
        mail, username, password = request.POST.dict().values
        message: dict = get_route_params("signup")
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