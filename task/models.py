from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    address_line1 = models.CharField(max_length=255)
    address_city = models.CharField(max_length=100)
    address_state = models.CharField(max_length=100)
    address_pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


