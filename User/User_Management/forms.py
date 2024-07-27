from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email',
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username',
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm your password',
            }),
        }
        labels = {
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password',
            }),
        }
        labels = {
            'username': 'Username',
            'password': 'Password',
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['room_number', 'bed_number', 'mobile_number', 'profile_picture', 'aadhar_card', 'pan_card', 'bio']
        widgets = {
            'room_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter room number',
            }),
            'bed_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter bed number',
            }),
            'mobile_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter mobile number',
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'aadhar_card': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'pan_card': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your bio',
                'rows': 4,
            }),
        }
        labels = {
            'room_number': 'Room Number',
            'bed_number': 'Bed Number',
            'mobile_number': 'Mobile Number',
            'profile_picture': 'Profile Picture',
            'aadhar_card': 'Aadhar Card',
            'pan_card': 'PAN Card',
            'bio': 'Bio',
        }
