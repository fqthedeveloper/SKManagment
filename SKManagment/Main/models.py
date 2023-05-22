from django.db import models

# Create your models here.


class Appointment(models.Model) :
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email_subject = models.CharField(max_length=200)
    Message = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.full_name
