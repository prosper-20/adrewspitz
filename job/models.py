from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

JOB_CHOICES =(
    ("Remote", "Remote"),
    ("On site", "On site")
)

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    salary = models.CharField(max_length=200, blank=True, null=True)
    company = models.CharField(max_length=100)
    type = models.CharField(choices=JOB_CHOICES, max_length=200)

    def __str__(self):
        return self.title
    

ID_DOCUMENT_CHOICES = [
        ("Driver's License", 'Driver\'s License'),
        ('Passport', 'Passport'),
        ('State ID', 'State ID'),
    ]

GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Others")
]

JOB_TYPE = [
    ("Personal Assistant", "Personal assistant"),
    ("Data Entry", "Data Entry"),
    ("Mystery Shopper", "Mystery Shopper"),
    ("Virtual Assistant", "Virtual Assistant")
]

class Applicant(models.Model):
    First_name = models.CharField(max_length=100)
    Middle_name = models.CharField(max_length=100, blank=True, null=True)
    Last_name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    Home_address = models.CharField(max_length=300)
    Phone_number = PhoneNumberField()
    email = models.EmailField()
    Job_aspired = models.CharField(max_length=100,choices=JOB_TYPE)
    Id_document = models.CharField(max_length=100, choices=ID_DOCUMENT_CHOICES)
    Id_image = models.ImageField(upload_to="Documents", blank=True, null=True)
    Former_workplace = models.CharField(max_length=200, blank=True, null=True)
    Workplace_address = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.First_name} {self.Last_name}"
