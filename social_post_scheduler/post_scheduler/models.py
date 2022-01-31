from django.db import models
from django.utils import timezone

# Create your models here.

class Posts(models.Model):
    caption = models.CharField(max_length=1000)
    comment = models.CharField(max_length=1000)
    image = models.ImageField()
    ts_created = models.DateTimeField(default=timezone.now)
    ts_schedule = models.DateTimeField()
