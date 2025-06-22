from django.db import models
from django.conf import settings

class Alert(models.Model):
    AGRICULTURE_TYPES = (
        ('crop', 'Crop'),
        ('livestock', 'Livestock'),
        ('other', 'Other'),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    agriculture_type = models.CharField(max_length=20, choices=AGRICULTURE_TYPES)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author.username}"