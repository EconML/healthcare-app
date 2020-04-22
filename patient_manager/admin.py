from django.contrib import admin
from .models import Patient, Condition, Servicerequest, Clinicalmeasures

# Register your models here.
admin.site.register(Patient)
admin.site.register(Condition)
admin.site.register(Servicerequest)
admin.site.register(Clinicalmeasures)
