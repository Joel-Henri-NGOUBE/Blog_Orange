from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog', views.articles, name="blog"),
    path('logout', views.logout, name="logout"),
    path('chat', views.Chat.as_view(http_method_names=['get', 'post']), name="chat"),
    path('newpost', views.NewPost.as_view(http_method_names=['get', 'post']), name="newpost"),
    path('login', views.Login.as_view(http_method_names=['get', 'post']), name="login"),
    path('signup', views.Signup.as_view(http_method_names=['get', 'post']), name="signup")
]