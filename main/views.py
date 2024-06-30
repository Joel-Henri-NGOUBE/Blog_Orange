from django.shortcuts import render, redirect, resolve_url
from .models import Article, User
from django.utils.translation import gettext
from django.views import View
from .utils.utils_functions import get_route_params
from django.contrib.auth.hashers import make_password, check_password
from gpt4all import GPT4All
from langchain_community.embeddings import GPT4AllEmbeddings

# from pathlib import Path
# from os.path import join

# BASE_DIR = Path(__file__).resolve().parent.parent

model_name = "all-MiniLM-L6-v2-f16.gguf"

# model_path = BASE_DIR / "LLM"
# print(model_path)
# model_path = join(BASE_DIR, "/LLM/all-MiniLM-L6-v2-f16.gguf")
# print(model_path)

def home(request):
    return redirect(resolve_url("blog"))

def articles(request):
    bonjour = gettext("bonjour")
    articles = Article.objects.all()
    context: dict = get_route_params("blog", request)
    context["articles"] = articles
    # context["id"] = request.session["id"]
    return render(request, "articles/index.html", context = context)

def logout(request):
    if request.session.get("id"):
        request.session.flush()
        return redirect(resolve_url("login"))


class Chat(View):
    def get(self, request):
        context: dict = get_route_params("chat", request)
        return render(request, "chat/index.html", context = context)
    def post(self, request):
        question = request.POST.get("question")
        embeddings = GPT4AllEmbeddings(model_name=model_name)
        response = embeddings.embed_query(question)
        # model = GPT4All(model_name=model_name)
        # response = model.generate(question, max_tokens=500)
        context: dict = get_route_params("chat", request)
        context["response"] = response
        return render(request, "chat/index.html", context = context)
    
class NewPost(View):
    def get(self, request):
        if request.session.get("id"):
            context: dict = get_route_params("newpost", request)
            return render(request, "newpost/index.html", context = context)
        return redirect(resolve_url("login"))
    
    def post(self, request):
        id = request.session.get("id")
        if id:
            _, title, description = request.POST.dict().values()
            user = User.objects.filter(id=id)[0]
            Article.objects.create(
                title = title,
                content = description,
                user = user
            )
            context: dict = get_route_params("newpost", request)
            context["message"] = "Publication ajoutée avec succès"
            return render(request, "newpost/index.html", context = context)
        return redirect(resolve_url("login"))
        

class Login(View):
    def get(self, request):
        if not (request.session.get("id")):
            context: dict = get_route_params("login", request)
            return render(request, "login/index.html", context = context)
        return redirect(resolve_url("blog"))
    
    def post(self, request):
        if not (request.session.get("id")):
            _, mail, password = request.POST.dict().values()
            message: dict = get_route_params("login", request)
            if mail and password:
                user = User.objects.filter(mail=mail).values()
                print(user)
                if(len(user)):
                    id, username, mail, real_password = user[0].values()
                    if check_password(password, real_password):
                        request.session["id"] = id
                        request.session["username"] = username
                        request.session["mail"] = mail
                        return redirect(resolve_url("blog"))
                    else:
                        message["error"] = "Mot de passe incorrect"
                        return render(request, "login/index.html", context = message) 
                else:
                    message["error"] = "Utilisateur introuvable"
                    return render(request, "login/index.html", context = message) 
            message["error"]  = "Un ou plusieurs champs non renseignés"
            return render(request, "login/index.html", context = message)
        return redirect(resolve_url("blog"))   
    
class Signup(View):
    def get(self, request):
        if not (request.session.get("id")):
            context: dict = get_route_params("signup", request)
            return render(request, "signup/index.html", context = context)
        return redirect(resolve_url("blog"))
    
    def post(self, request):
        if not (request.session.get("id")):
            print(request.POST.dict().values())
            _, mail, username, password = request.POST.dict().values()
            message: dict = get_route_params("signup", request)
            if mail and username and password:
                user = User.objects.filter(mail=mail)
                print(user)
                if(len(user)):
                    message["error"] = "Adresse mail déjà utilisée"
                    return render(request, "signup/index.html", context = message) 
                else:
                    User.objects.create(
                    mail = mail,
                    username = username,
                    password = make_password(password)
                )
                    message["success"] = "Utilisateur créé avec succès"
                    return render(request, "signup/index.html", context = message) 
            message["error"]  = "Un ou plusieurs champs non renseignés"
            return render(request, "signup/index.html", context = message)
        return redirect(resolve_url("blog"))
    
        # print(request.body.decode())
        # print(list(request.POST.items()))
        # print(dict(request.POST.items())) 