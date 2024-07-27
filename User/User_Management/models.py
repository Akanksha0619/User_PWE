# models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # New fields
    room_number = models.CharField(max_length=100, blank=True, null=True)
    bed_number = models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='default.jpg')
    aadhar_card = models.FileField(upload_to='documents/aadhar/', blank=True, null=True)
    pan_card = models.FileField(upload_to='documents/pan/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
