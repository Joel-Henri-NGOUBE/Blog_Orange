from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.articles),
    path('login', views.Login.as_view(http_method_names=['get', 'post'])),
    path('signup', views.Signup.as_view(http_method_names=['get', 'post']))
]