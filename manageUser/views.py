from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def about(request):
       if request.method == 'POST':
        u = User.objects.get(username=request.user)
        email = request.POST['email']
        u.email=email
        u.save()
        return HttpResponse(request.POST['email'])
       else: 
         return render(request, 'pages/about.html')