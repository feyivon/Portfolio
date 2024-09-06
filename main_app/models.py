from django.db import models

# Create your models here.
class Description(models.Model):
    subject = models.CharField(max_length= 1000)
    description=models.TextField()