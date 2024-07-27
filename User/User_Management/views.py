from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.urls import reverse


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Profile is created automatically via signal
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html', {'profile': request.user.profile})


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

def index(request):
    context = {
        'current_page': reverse('index'),
        # other context variables
    }
    return render(request, 'landing.html', context)


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after updating
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'update_profile.html', {'form': form})

def profile(request):
    user = request.user
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = None  # Or handle this case as needed

    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def profile(request):
    user = request.user
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = None  # Or handle this case as needed

    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)

from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # Other URL patterns
    path('logout/', LogoutView.as_view(), name='logout'),
]
