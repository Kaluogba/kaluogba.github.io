from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="index")
        path('login/', views.login_page, name='login'),
        path('logout/', views.logout_user, name='logout'),
        path('register/', views.register_page, name='register'),
        path('profile/', views.profile_page, name='profile'),
        path('password-reset/', views.password_reset_page, name='password_reset'),
        path('email-verification/', views.email_verification_page, name='email_verification'),
        path('dashboard/', views.dashboard_page, name='dashboard'),
        path('api/user-info/', views.user_info_api, name='user_info_api'),
]
