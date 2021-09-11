from django.db import models

Genders=[('Male','Male'), ('Female','Female'), ('Other', 'Other')]

class DoctorModel(models.Model):
  name=models.CharField(max_length=30)
  gender=models.CharField(max_length=6,choices=Genders,default='Male')
  dob=models.DateField()
  age=models.CharField(max_length=2)
  mobile_Number=models.CharField(max_length=10)
  email=models.EmailField(max_length=30,unique=True)
  upload_photo=models.ImageField(upload_to='images/',default="default/default_img.jpg")
  password=models.CharField(max_length=8)
  repeat_password=models.CharField(max_length=8)
  hospital_name=models.CharField(max_length=30)
  hospital_address=models.CharField(max_length=60)
  hospital_registartion_id=models.CharField(max_length=10)
  hospital_registartion_id_Proof=models.ImageField(upload_to='images/', default="images/default_img.jpg")
