from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('triple', 'Triple'),
    ]

    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    capacity = models.IntegerField()
    price_per_month = models.DecimalField(max_digits=8, decimal_places=2)
    amenities = models.TextField(help_text="List of amenities, separated by commas")
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)

    def __str__(self):
        return f"Room {self.room_number} ({self.get_room_type_display()})"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    inquiry = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} booking {self.room.room_number} from {self.start_date} to {self.end_date}"
