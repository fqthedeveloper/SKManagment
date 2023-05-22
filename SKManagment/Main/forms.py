from django import forms
from . import models


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = models.Appointment
        fields = ('full_name', 'email', 'phone_number', 'email_subject', 'Message')
