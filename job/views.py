from django.shortcuts import render
from .models import Job, Applicant
from django.contrib import messages
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage

def home(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("Gender")
        email = request.POST.get("email")
        home_address = request.POST.get("home_address")
        phone_number = request.POST.get("phone_number")
        job_interest = request.POST.get("job_aspired")
        valid_id = request.POST.get("valid_id")
        image = request.FILES.get("image")
        previous_place = request.POST.get("previous_workplace")

        Applicant.objects.create(First_name=first_name, Middle_name=middle_name, 
                                 Last_name=last_name, Gender=gender, 
                                 email=email, Home_address=home_address, Phone_number=phone_number,
                                 Job_aspired=job_interest, Id_document=valid_id, Id_image=image,
                                 Former_workplace=previous_place)
        messages.success(request, "Application Info submitted")

    return render(request, "job/index.html")



