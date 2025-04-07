from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='picture/%Y/%m/%d')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'