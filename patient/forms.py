from django import forms
from .models import PatientModel

class RegistrationForm(forms.ModelForm):
  gender_choices = [('Male', 'Male'), ('Female', 'Female')]
  password = forms.CharField(widget=forms.PasswordInput)
  phone = forms.CharField(max_length=10)
  # gender = forms.ChoiceField(choices=gender_choices) # DropDown
  gender = forms.CharField(widget=forms.RadioSelect(choices=gender_choices))
  # dob = forms.CharField(widget=forms.DateInput)
  class Meta:
    model = PatientModel
    fields = "__all__"

class LoginForm(forms.Form):
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)