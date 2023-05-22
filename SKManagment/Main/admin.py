from django.contrib import admin
from . import models

# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'send_time')

admin.site.register(models.Appointment, AppointmentAdmin)