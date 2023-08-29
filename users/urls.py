from django.urls import path
from rest_framework import routers
from users.views import UtilisateurView, ClientView

router = routers.DefaultRouter()

# router.register('use_api', UtilisateurView)
# router.register('cli_api', ClientView)
# urlpatterns = [
#     path("users/", UtilisateurView.as_view(), name="use_api"),
#     path("client/", ClientView.as_view(), name="cli_api"),
# ]
