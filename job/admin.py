from django.contrib import admin
from .models import Job, Applicant


admin.site.register([Job, Applicant])
