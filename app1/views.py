from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
import random
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login as auth_login
from .models import *
from django.contrib.auth.decorators import login_required

def login_new(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('login_new')
    return render(request, 'login.html')

