from django.db import models

# Create your models here.
class PatientModel(models.Model):
  name = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  email = models.EmailField()
  gender = models.CharField(max_length=50)
  image = models.ImageField(upload_to="images", default="images/test.jpg")
  phone = models.IntegerField()
  age = models.IntegerField()