from django.db import models


# Create your models here.
Genders=[
            ('Male','Male'),
            ('Female','Female')
        ]
class DoctorModel(models.Model):
         Name=models.CharField(max_length=30)
         Gender=models.CharField(max_length=6,choices=Genders,default='Male')
         DOB=models.DateField()
         Age=models.CharField(max_length=2)
         Mobile_Number=models.CharField(max_length=10)
         Email=models.EmailField(max_length=30,unique=True)
         Upload_Photo=models.ImageField(upload_to='images/',default="default/default_img.jpg")
         Password=models.CharField(max_length=8)
         Repeat_Password=models.CharField(max_length=8)
         Hospital_Name=models.CharField(max_length=30)
         Hospital_Address=models.CharField(max_length=60)
         Hospital_Registartion_ID=models.CharField(max_length=10)
         Hospital_Registartion_ID_Proof=models.ImageField(upload_to='images/', default="default/default_img.jpg")
