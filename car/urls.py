from django.urls import path
from . import views

app_name = 'car'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.log, name='login'),
    path('forgot/', views.forgot, name='forgot'),
    path('index/', views.index, name='index'),
    path('logout/', views.user_logout, name='logout'),
    path('post/', views.post_car, name='post'),
]