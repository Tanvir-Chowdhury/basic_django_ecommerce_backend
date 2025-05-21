from django.db import models
from django.contrib.auth.models import AbstractUser


USER_OPTIONS = (
    ('user', 'User'),
    ('admin', 'Admin'),
    ('super-admin', 'Super-admin'),
)

# Create your models here.
class SiteUser(AbstractUser):
    shipping_address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    special_user = models.CharField(max_length=20, choices=USER_OPTIONS, default='user') 

    def __str__(self):
        return self.username
    
    class Meta:
        unique_together = ('email', 'username') 