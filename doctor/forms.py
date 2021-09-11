from django.forms.widgets import DateInput
from doctor.models import DoctorModel
from django import forms

class DocterLoginForm(forms.Form):   
  email=forms.EmailField()
  password=forms.CharField(widget=forms.PasswordInput())

class DateInput(forms.DateInput):
  input_type='date'

class RegistrationForm(forms.ModelForm):
  def clean(self):
    cleaned_data=super().clean()
    f_pass=cleaned_data['password']
    c_pass=cleaned_data['repeat_password']
    if f_pass != c_pass:
      raise forms.ValidationError('Password Not Match')

    hospital_address=forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":15}))
    class Meta:
      model=DoctorModel
      fields='__all__'

      widgets={
        'dob':DateInput(),
      }

