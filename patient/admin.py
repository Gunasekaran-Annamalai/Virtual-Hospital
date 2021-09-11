from django.contrib import admin

# Register your models here.

from .models import PatientModel

admin.site.register(PatientModel)