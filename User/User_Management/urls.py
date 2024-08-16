from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
    path('logout/', logout, name='logout'),
    path('subscribe/', subscribe, name='subscribe'),

    
]
