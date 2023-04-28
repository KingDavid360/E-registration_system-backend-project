from django.db import models
from django.contrib.auth.models import User

class ClientModel(models.Model):
    staff_id=models.CharField(max_length=20, blank=True)
    nin=models.CharField(max_length=10, blank=True)
    email=models.CharField(max_length=50,blank=True)
    first_name=models.CharField(max_length=15, blank=True)
    last_name=models.CharField(max_length=15, blank=True)
    middle_name=models.CharField(max_length=15, blank=True)
    gender=models.CharField(max_length=10, blank=True)
    phone_number=models.CharField(max_length=11,blank=True)
    birthday=models.DateField(blank=True)
    institution=models.CharField(max_length=15, blank=True)
    type_of_institution=models.CharField(max_length=15, blank=True)
    address=models.TextField(blank=True)
    city=models.CharField(max_length=15, blank=True)
    state=models.CharField(max_length=15, blank=True)
    grade_level=models.CharField(max_length=10, blank=True)
    course=models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.staff_id

