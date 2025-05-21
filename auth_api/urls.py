from django.urls import path

from auth_api.views.login import LoginView
from auth_api.views.register import RegisterUsersView

urlpatterns = [
    path("register", RegisterUsersView.as_view(), name="Register"),
    path("login", LoginView.as_view(), name="Login"),
]