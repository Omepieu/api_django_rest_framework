from django.contrib import admin
from users.models import Utilisateur, Client

# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Client)