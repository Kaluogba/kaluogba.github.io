from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'data/index.html')

def login_page(request):
    return render(request, 'data/login.html')

def logout_user(request):
    # Logic to log out the user
    return render(request, 'data/logout.html')

def register_page(request):
    return render(request, 'data/register.html')

def profile_page(request):
    # Logic to retrieve and display user profile information
    return render(request, 'data/profile.html')

def password_reset_page(request):
    # Logic for password reset functionality
    return render(request, 'data/password_reset.html')

def email_verification_page(request):
    # Logic for email verification functionality
    return render(request, 'data/email_verification.html')

def dashboard_page(request):
    # Logic to retrieve and display user dashboard
    return render(request, 'data/dashboard.html')

def user_info_api(request):
    # Logic to serve JSON data containing user information
    return render(request, 'data/user_info_api.html')

