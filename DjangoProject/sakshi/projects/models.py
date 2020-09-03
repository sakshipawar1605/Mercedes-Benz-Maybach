from django.db import models

# Create your models here.
class Projects(models.Model):
    name=models.CharField(max_length=200)
    details=models.CharField(max_length=500)

    image=models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=100)