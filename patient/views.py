from django.shortcuts import redirect, render
from django.views.generic import View

from .models import PatientModel
from .forms import RegistrationForm, LoginForm
# Create your views here.

class CreateAccountView(View):
  def get(self, request):
    form = RegistrationForm()
    return render(request,"patient/registration.html", {
      "form": form,
      "error": None
    })

  def post(self, request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
      try:
        PatientModel.objects.all().get(email=form.cleaned_data["email"])
        return render(request,"patient/registration.html", {
          "form": form,
          "error": "Mail Id already exists"
        })
      except:
        form.save()
      return redirect("/patient/thank-you")

class LoginView(View):
  def get(self, request):
    form = LoginForm()
    return render(request, "patient/login_form.html", {
      "form": form
    })

  def post(self, request):
    form = LoginForm(request.POST) # storing form data in form variable
    
    if form.is_valid():
      form_data = form.cleaned_data
      email = form_data["email"]
      password = form_data["password"]
      try:
        PatientModel.objects.all().get(email=email, password=password)
      except:
        print("Error")
        return render(request, "patient/login_form.html", {
          "form": form,
          "error": "Email Id or Password must be wrong."
        })

      return redirect("/patient/thank-you")
    
    return render(request, "patient/login_form.html", {
      "form": form
    })

class ThankyouView(View):
  def get(self, request):
    return render(request, "patient/thankyou.html")