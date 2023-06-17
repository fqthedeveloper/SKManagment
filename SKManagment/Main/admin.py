from django.contrib import admin
from . import models

# Register your models here.

class AdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')

admin.site.register(models.Admin, AdminAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'send_time')

admin.site.register(models.Appointment, AppointmentAdmin)