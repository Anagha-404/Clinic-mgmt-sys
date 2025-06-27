from django.contrib import admin
from .models import Department,Doctor,Prescription,Medicine,LabTest,Receptionist,UserDetails,Patient,Appointment
# Register your models here.

admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Prescription)
admin.site.register(Medicine)
admin.site.register(LabTest)
admin.site.register(Receptionist)
admin.site.register(UserDetails)
admin.site.register(Patient)
admin.site.register(Appointment)
