
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Signup, Post
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random

global context

def signup(request):
    if request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['phone_number']

        user = Signup.objects.create(first_name=first_name, last_name=last_name,email=email, password=password, phone_number=phone_number)
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


all_cars = Post.objects.all()
car_list = []
for car in all_cars:
    car_list.append(car)

global random_car
global random_car2
def index(request):
    global random_car
    global random_car2
    random_car = random.choice(car_list)
    random_car2 = random.choice(car_list)
    print(random_car.image)
    context = {
        'random_car': random_car,
        'random_car2': random_car2,
    }
    return render(request, 'car/index.html', context=context)


def user_logout(request):
    logout(request)
    return redirect(reverse('car:login'))


def post_car(request):
    if request.POST:
        model = request.POST['model']
        price = request.POST['price']
        car_make = request.POST['car_make']
        body_type = request.POST['body_type']
        transmission = request.POST['transmission']
        year = request.POST['year']
        color = request.POST['color']
        description = request.POST['description']
        image_file = request.FILES['image']
        phone_number = request.POST['phone_number']

        user = request.user

        new_post = Post(user=user, model=model, price=price, car_make=car_make, body_type=body_type,
                        transmission=transmission, year=year, color=color, description=description, image=image_file, phone_number=phone_number)
        new_post.save()

        return redirect(reverse('car:index'))
    else:
        return render(request, 'car/post.html')


def detail(request):
    global random_car
    global random_car2
    car = random_car or random_car2
    if car == random_car:
        car = random_car
    else:
        car = random_car2
    context_detail = {
        'car': car,
    }

    return render(request, 'car/detail.html', context=context_detail)
