from django.contrib import admin
from .models import ProfileInfo, PasswordResetToken, EmailVerificationToken

# Register your models here.

@admin.register(ProfileInfo)
class ProfileInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location', 'website')
    search_fields = ('user__username', 'user__email')

@admin.register(PasswordResetToken)
class PasswordResetTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'expiration')
    search_fields = ('user__username', 'user__email')

@admin.register(EmailVerificationToken)
class EmailVerificationTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'expiration', 'verified')
    search_fields = ('user__username', 'user__email')

