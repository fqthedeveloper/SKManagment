from django.http import JsonResponse
from .serializers import AdminSerializer, AppointmentSerializer
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from . import models


class AdminList(generics.ListCreateAPIView) :
    queryset = models.Admin.objects.all()
    serializer_class = AdminSerializer
    #permission_classese = [permissions.IsAuthenticated]


class adminDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = models.Admin.objects.all()
    serializer_class = AdminSerializer
    #permission_classese = [permissions.IsAuthenticated]


@csrf_exempt
def admin_login(request) :
    email = request.POST.get('email')
    password = request.POST.get('password')

    try :
        adminData = models.Admin.objects.get(email=email, password=password)

    except models.Admin.DoesNotExist :
        adminData = None

    if adminData :
        return JsonResponse({'bool' :True, 'user_id' :adminData.id})
    else :
        return JsonResponse({'bool' :False})


class Appointment(generics.ListCreateAPIView):
    queryset = models.Appointment.objects.all()
    serializer_class = AppointmentSerializer