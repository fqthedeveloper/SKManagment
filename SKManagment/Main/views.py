from django.shortcuts import render, redirect
from . import forms


def home(request) :
    return render(request, 'home.html')


def contact(request) :
    msg = ''
    if request.method == 'POST' :
        form = forms.AppointmentForm(request.POST)
        if form.is_valid() :
            form.save()
            msg = 'Data Has Been Saved'
    form = forms.AppointmentForm
    return render(request, 'contact.html', {'form':form, 'msg':msg})


def about(request) :
    return render(request, 'aboutus.html')


def services(request) :
    return render(request, 'services.html')

