from django.urls import path
from .views import   doctorregistration ,doctorlogin
urlpatterns = [
    path("create-account",doctorregistration.as_view()),
    path("login",doctorlogin.as_view())
]