from django.shortcuts import render, HttpResponse, redirect

# for authentication purposes
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        formData = request.POST
        username = formData['username']
        password1 = formData['password1']
        password2 = formData['password2']
        if password1 == "" or password2 == "":
            return render(request, 'account/signup.html', {'error': 'password cannot be empty'})
        elif password1 == password2:
            if User.objects.filter(username = username).first() != None:
                return render(request, 'account/signup.html', {'error': 'username has alrealy been taken'})
            else:
                user = User.objects.create_user(username, password = password1)
                auth.login(request, user)
                return redirect('index')
        else:
            return render(request, 'account/signup.html', {'error': 'passwords do not match'})
    return render(request, 'account/signup.html')

def login(request):
    return render(request, 'account/login.html')

def logout(request):
    return HttpResponse('logout')
