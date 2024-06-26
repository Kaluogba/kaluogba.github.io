from django.shortcuts import render,redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from .models import ProfileInfo
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'data/index.html')

def login_page(request):
    if request.method == 'POST':
        # Retrieve username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User authentication successful, log in the user
            login(request, user)
            # Redirect to a different page after login (e.g., dashboard)
            return redirect('dashboard')
        else:
            # Authentication failed, render the login page with an error message
            return render(request, 'data/login.html', {'error_message': 'Invalid username or password'})

    # If the request method is GET, render the login page
    return render(request, 'data/login.html', context_instance=RequestContext(request))

def logout_user(request):
    # Logic to log out the user
    return render(request, 'data/logout.html')

def register_page(request):
    if request.method == 'POST':
        # Extract form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate and process the data
        if password != confirm_password:
            return render(request, 'data/register.html', {'error_message': 'Passwords do not match'})

        # Check if a user with the same username or email already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return render(request, 'data/register.html', {'error_message': 'Username or email already exists'})

        # Create a new user
        new_user = User.objects.create_user(username=username, email=email, password=password)

        # Create a corresponding UserProfile instance
        UserProfile.objects.create(user=new_user)

        # Redirect to login page or any other page
        return redirect('login')
    else:
        # Render the registration form
        return render(request, 'data/register.html')

def chart_data(request):
    # Retrieve data from your data source (e.g., database)
    data = YourModel.objects.all()

    # Prepare the data in the format required by Chart.js
    labels = []
    values = []

    for item in data:
        labels.append(item.label_field)  # Assuming label_field is a field in your model
        values.append(item.value_field)  # Assuming value_field is a field in your model

    # Construct the chart data dictionary
    chart_data = {
        'labels': labels,
        'datasets': [{
            'label': 'Your Dataset Label',
            'data': values,
            'backgroundColor': 'rgba(75, 192, 192, 0.2)',  # Example background color
            'borderColor': 'rgba(75, 192, 192, 1)',         # Example border color
            'borderWidth': 1                                 # Example border width
        }]
    }

    # Return the chart data as JSON response
    return JsonResponse(chart_data)

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

