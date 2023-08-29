from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Client, Utilisateur

# class UserSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'password1',
#             'password2'
#         ]
class UtilisateursSerializers(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = [
            'nom',
            'prenom',
            'email',
            'password',
            'date_de_nais',
            'lieu_de_nais',
            'genre',
            'contact'
            ]
        
class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Client
        fields = [
            'utilisateur_id',
            'nom',
            'prenom',
            'email',
            'password',
            'date_de_nais',
            'lieu_de_nais',
            'genre',
            'contact'
            ]
