from email.policy import default
from django.db import models
from datetime import datetime
# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(default=datetime.now())