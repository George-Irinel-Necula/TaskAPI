from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#Definesc inca un camp pt User
class User(AbstractUser):
    age=models.PositiveIntegerField(default=18,blank=False)

    def __str__(self): #Arata atat in interfata de Django-Admin titlul cat si daca am o relatie sa selectez username-ul in loc de PK
        return f"{self.username}"

class Tasks(models.Model):
    title=models.CharField(max_length=255,blank=False)
    description=models.CharField(blank=False)
    date_created=models.DateField(auto_now_add=True)
    completed=models.BooleanField(default=1)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='tasks')

    def __str__(self):
        return self.title
    
