from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.AdminList.as_view()),

    path('admin/<int:pk>/', views.adminDetail.as_view()),

    path('admin-login', views.admin_login),

    path('appointment/', views.Appointment.as_view()),

]