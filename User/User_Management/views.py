from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import RegisterForm, LoginForm
from .forms import ProfileUpdateForm
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from io import BytesIO
from reportlab.lib.pagesizes import letter
import io
from django.core.mail import send_mail, EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from reportlab.pdfgen import canvas
from .models import Subscription


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


def logout(request):
    messages.info(request, 'you have logged out.')
    return redirect('index')

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

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')


def generate_pdf(email):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 750, "Subscription Confirmation")
    p.drawString(100, 725, f"Thank you for subscribing, {email}.")
    p.drawString(100, 700, "We have successfully received your subscription request.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer



@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            subscription, created = Subscription.objects.get_or_create(email=email)
            if created:
                try:
                    # Send notification email to admin
                    send_mail(
                        'New Subscription',
                        f'A new subscription request has been received from {email}.',
                        'akankshamarathe19@gmail.com',
                        ['akankshamarathe19@gmail.com'],
                        fail_silently=False,
                    )

                    # Generate PDF
                    pdf_buffer = generate_pdf(email)

                    # Plain text email body
                    email_subject = "Subscription Confirmation"
                    email_body = f"Dear {email},\n\nThank you for subscribing to our service. Please find attached a confirmation PDF with your subscription details.\n\nBest regards,\nYour Company Name"
                    email_message = EmailMessage(
                        email_subject,
                        email_body,
                        'akankshamarathe19@gmail.com',
                        [email],
                    )
                    email_message.attach('subscription_details.pdf', pdf_buffer.read(), 'application/pdf')
                    email_message.send()

                    return JsonResponse(
                        {'status': 'success', 'message': 'Subscription successful. Check your email for confirmation.'})
                except Exception as e:
                    return JsonResponse({'status': 'error', 'message': f'Failed to send email: {str(e)}'}, status=500)
            else:
                return JsonResponse({'status': 'error', 'message': 'You have already subscribed.'}, status=400)

        return JsonResponse({'status': 'error', 'message': 'Email not provided.'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)


def generate_pdf(email):
    pdf_buffer = io.BytesIO()
    p = canvas.Canvas(pdf_buffer)
    p.drawString(100, 750, f"Subscription Confirmation")
    p.drawString(100, 730, f"Thank you for subscribing to our service.")
    p.drawString(100, 710, f"Email: {email}")
    p.showPage()
    p.save()
    pdf_buffer.seek(0)  # Move buffer position to the start
    return pdf_buffer
