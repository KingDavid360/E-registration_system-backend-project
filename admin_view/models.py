from django.db import models
from django.contrib.auth.models import User

class AdminProfile(models.Model):
    owner = models.ForeignKey(User, related_name='admin_account', on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.email

