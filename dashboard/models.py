from django.db import models

from django.db import models
from django.db import models
from django.contrib.auth.models import User

TYPE =(
    ('Materiel','Materiel'),
    ('Logiciel','Logiciel'),
)

STATUT =(
    ('NON RESOLUE','NON RESOLUE'),
    ('ENCOURS','ENCOURS'),
    ('RESOLUE','RESOLUE'),
)

# Create your models here.


class User(models.Model):

    id_user = models.CharField(max_length=100)
    nom = models.CharField(max_length=200)
    numtel = models.CharField(max_length=50)
    adresse = models.CharField(max_length=100)
    email = models.EmailField()


class Problem(models.Model):
  
    NomProblem = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=20, choices=TYPE, null=True)
    statut = models.CharField(max_length=20, choices=STATUT, null=True)

    def __str__(self):
        return f'{self.NomProblem}-{self.type}'
    
class Intervention(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    NomInterven= models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add= True)

    def __str(self):
        return f'{self.NomInterven}' 
    




class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.title}"

    



   