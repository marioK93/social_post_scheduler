from pyexpat import model
from django.db import models
from django.utils.timezone import datetime

# Create your models here.

class Posts(models.Model):
    caption = models.CharField(max_length=1000)
    comment = models.CharField(max_length=1000)
    image = models.ImageField()
    ts_created = models.DateTimeField(default=datetime.now)
    ts_schedule = models.DateTimeField()
