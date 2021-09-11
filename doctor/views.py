from django.contrib import messages
from django.http import response
from django.shortcuts import render,redirect
from doctor.forms import RegistrationForm,DocterLoginForm
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
      form=DocterLoginForm()
      return render(request,'doctor/login.html',context={'form':form})
    def post(self,request):
      form=DocterLoginForm()
      if DoctorModel.objects.filter(email=request.POST['email'],password=request.POST['password']).exists():
        Doctor=DoctorModel.objects.get(email=request.POST['email'],password=request.POST['password'])
        return render(request,'doctor/test.html',{'Doctor':Doctor})
      else:
        messages.error(request,'Invalid Email / Password')
        return render(request,'doctor/login.html',context={'form':form})
            




    