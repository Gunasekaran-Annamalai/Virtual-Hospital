from django.urls import path
from . import views

urlpatterns = [
  path("create-account/", views.CreateAccountView.as_view()),
  path("thank-you", views.ThankyouView.as_view()),
  path("login", views.LoginView.as_view())
]