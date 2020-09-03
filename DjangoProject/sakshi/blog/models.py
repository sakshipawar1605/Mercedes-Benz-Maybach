from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    date=models.DateField(auto_now=False,auto_now_add=False)
    image=models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)


class Gallery(models.Model):
    event=models.CharField(max_length=200)

