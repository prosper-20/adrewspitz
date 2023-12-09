from django.db.models.signals import post_save
from .models import Applicant
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMessage
from decouple import config
from django.conf import settings
from django.template.loader import render_to_string

# @receiver(post_save, sender=Applicant)
# def send_registration_email(sender, instance, created, **kwargs):
#     if created:
#         subject = 'Application Received'
#         message = 'Thank you for registering on our platform. We hope you enjoy your experience!'
#         from_email = settings.DEFAULT_FROM_EMAIL # Replace with your email
#         to_email = [instance.email]

#         send_mail(subject, message, from_email, to_email)


@receiver(post_save, sender=Applicant)
def send_registration_mail(sender, instance, created, **kwargs):
    if created:
        subject = "Exciting Remote Personal Assistant Opportunity - $40/hr"
        context = {
            'first_name': instance.First_name,
        }
        message = render_to_string('job/modified_email.html', context) 
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [instance.email]
        # send_mail(subject, message, from_email, to_email)
        msg = EmailMessage(subject, message, from_email, to_email)
        msg.content_subtype = 'html'
        msg.send()