from django.db import models
from django.contrib.auth.models import User

class ClientModel(models.Model):
    owner = models.ForeignKey(User, related_name='client', on_delete=models.CASCADE,null=True)
    staff_id=models.CharField(max_length=20, blank=True)
    nin=models.CharField(max_length=15, blank=True)
    first_name=models.CharField(max_length=15, blank=True)
    last_name=models.CharField(max_length=15, blank=True)
    middle_name=models.CharField(max_length=15, blank=True)
    gender_option = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    gender=models.CharField(max_length=10, blank=True, choices=gender_option)
    birthday=models.DateField()
    institution=models.CharField(max_length=100, blank=True)
    type_of_institution=models.CharField(max_length=100, blank=True)
    address=models.TextField(blank=True)
    city=models.CharField(max_length=100, blank=True)
    state=models.CharField(max_length=100, blank=True)
   

    def __str__(self):
        return self.staff_id

