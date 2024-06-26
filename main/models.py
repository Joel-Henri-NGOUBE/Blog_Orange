from django.db import models

# Create your models here. 
class User(models.Model):
    username: models.CharField = models.CharField(max_length=200)
    mail: models.EmailField = models.EmailField(null=True)
    password: models.CharField = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username
    
class Article(models.Model):
    title: models.CharField = models.CharField(max_length=200, null=False)
    content: models.TextField = models.TextField(null=False)
    publication_date: models.TimeField = models.DateTimeField(auto_now_add=True, null=False)
    user: models.ForeignKey = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.title

