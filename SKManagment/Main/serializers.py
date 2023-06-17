from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password

class AdminSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Admin
        fields = ['id','full_name', 'email', 'password']
        depth=1

class AppointmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Appointment
        fields = ['id','full_name', 'email', 'phone_number', 'email_subject', 'Message', 'send_time']
        depth=1
