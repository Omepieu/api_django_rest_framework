from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def produit_api_view(request, *args, **kwargs):
    data = {
        "name" : "orange",
        "price": 200,
        "descrip" :"bla bla bla"
    }

    return JsonResponse(data=data)

