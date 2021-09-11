from django.forms import fields
from django.forms.widgets import DateInput, Textarea
from doctor.models import DoctorModel
from django import forms

#Docter Login Form...
class docterloginform(forms.Form):   
    Email=forms.EmailField()
    Password=forms.CharField(widget=forms.PasswordInput())
   


#DOB FormField Method...
class DateInput(forms.DateInput):
    input_type='date'
  
#Docter Registration Form...
class RegistrationForm(forms.ModelForm):

#Password and Repeate Password Conform is same checking in Form side....
    def clean(self):
            cleaned_data=super().clean()
            f_pass=cleaned_data['Password']
            c_pass=cleaned_data['Repeat_Password']
            if f_pass != c_pass:
                raise forms.ValidationError('Password Not Match')
    
#Set FormSide Textarea
    Hospital_Address=forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":15}))
    
    class Meta:
        model=DoctorModel
        fields='__all__'

        
        #FormField Widgets...
        widgets={
            'DOB':DateInput(),
        }
    


