from django.urls import path
from . import views

app_name = 'car'

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log, name='login'),
    path('forgot/', views.forgot, name='forgot'),
    path('index/', views.index, name='index'),
]