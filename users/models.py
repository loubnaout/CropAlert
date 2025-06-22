from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Role(models.TextChoices):
        FARMER = 'FARMER', _('Farmer')
        AGRONOMIST = 'AGRONOMIST', _('Agronomist')
    
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.FARMER
    )
    
    class Meta:
        app_label = 'users'  
        
    def __str__(self):
        return self.username