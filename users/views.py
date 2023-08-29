from django.shortcuts import render
from rest_framework import viewsets, permissions

from users.models import Utilisateur, Client
from users.serializers import ClientSerializers, UtilisateursSerializers

# Create your views here.

class UtilisateurView(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateursSerializers
    permission_classes = [permissions.IsAuthenticated]

class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers