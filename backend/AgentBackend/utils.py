from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(user_email, verification_link):
    subject = 'Verify Your Email Address'
    message = f'Please verify your email address by clicking the following link: {verification_link}'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user_email])

def send_profile_update_notification(user_email):
    subject = 'Profile Update Notification'
    message = 'Your profile has been successfully updated.'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user_email])
