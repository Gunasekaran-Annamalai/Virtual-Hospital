from django.contrib import messages
from django.http import response
from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from doctor import forms
from doctor.forms import RegistrationForm,docterloginform
from django.contrib.auth.models import  auth
from doctor.models import DoctorModel
from django.views import View


# Create your views here

#Docter Registration codeing...
class doctorregistration(View):
    def get (self,request):
        form=RegistrationForm()
        return render(request,'doctor/registration.html',context={'form':form  })
    def post(self,request):
            form=RegistrationForm(request.POST,request.FILES)
            if form.is_valid():
                form.save() 
            return redirect('/doctor/login')
       
#Doctor login Codeing..
class doctorlogin(View):
    def get(self,request):
        form1=docterloginform()
        return render(request,'doctor/login.html',context={'form':form1})
    def post(self,request):
            form1=docterloginform()
            if DoctorModel.objects.filter(Email=request.POST['Email'],Password=request.POST['Password']).exists():
                Doctor=DoctorModel.objects.get(Email=request.POST['Email'],Password=request.POST['Password'])
                return render(request,'doctor/test.html',{'Doctor':Doctor})
            else:
                messages.error(request,'Invalid Email / Password')
                return render(request,'doctor/login.html',context={'form':form1})
            




    