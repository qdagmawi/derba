from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Signup
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Signup
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        user = Signup.objects.create(first_name=first_name, last_name=last_name,email=email, password=password)
        user.save()

        return redirect(reverse('car:login'))
    else:
        return render(request, 'car/signup.html')


def log(request):

    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        try:
            user = Signup.objects.get(email=email)

            if user.password == password:
                request.session['user_name'] = user.first_name

                return redirect(reverse('car:index'))
            else:
                return render(request, 'car/login.html', {'error': 'Invalid credentials'})
        except ObjectDoesNotExist:
            return render(request, 'car/login.html', {'error': 'User does not exist'})

    return render(request, 'car/login.html')


def forgot(request):
    return render(request, 'car/forgot.html')

@login_required
def index(request):
    return render(request, 'car/index.html')


def user_logout(request):
    logout(request)
    return redirect(reverse('car:login'))