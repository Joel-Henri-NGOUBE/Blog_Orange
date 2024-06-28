from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.articles, name="blog"),
    path('chat', views.Chat.as_view(http_method_names=['get', 'post']), name="chat"),
    path('newpost', views.NewPost.as_view(http_method_names=['get', 'post']), name="newpost"),
    path('login', views.Login.as_view(http_method_names=['get', 'post']), name="login"),
    path('signup', views.Signup.as_view(http_method_names=['get', 'post']), name="signup")
]