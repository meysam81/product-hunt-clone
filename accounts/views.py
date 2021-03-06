from django.shortcuts import render, HttpResponse, redirect

# for authentication purposes
from django.contrib.auth.models import User
from django.contrib import auth

from rest_framework import viewsets as vs
from .serializers import UserSerializer

def signup(request):
    if request.method == 'POST':
        formData = request.POST
        username = formData['username']
        password1 = formData['password1']
        password2 = formData['password2']
        if password1 == "" or password2 == "":
            return render(request, 'accounts/signup.html', {'error': 'password cannot be empty'})
        elif password1 == password2:
            if User.objects.filter(username = username).first() != None:
                return render(request, 'accounts/signup.html', {'error': 'username has alrealy been taken'})
            else:
                user = User.objects.create_user(username, password = password1)
                auth.login(request, user)
                return redirect('index')
        else:
            return render(request, 'accounts/signup.html', {'error': 'passwords do not match'})
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        formData = request.POST
        username = formData['username']
        password = formData['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect'})
    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')


class UserViewSet(vs.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer