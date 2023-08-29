from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Utilisateur(models.Model):
    date_de_nais = models.DateField(max_length=12)
    lieu_de_nais = models.CharField(max_length=200)
    CHOIX_GENRE = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    genre = models.CharField(max_length=1, choices=CHOIX_GENRE)
    contact = models.CharField(max_length=18)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)

    def __str__(self):
        self.nom

class Client(models.Model):
    utilisateur_id = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_de_nais = models.DateField(max_length=12)
    lieu_de_nais = models.CharField(max_length=200)
    CHOIX_GENRE = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    genre = models.CharField(max_length=1, choices=CHOIX_GENRE)
    contact = models.CharField(max_length=18)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)

    def __str__(self):
        self.utilisateur_id.nom


