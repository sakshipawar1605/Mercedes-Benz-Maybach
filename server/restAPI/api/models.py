from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    contact = models.CharField(max_length=200)
    doa = models.CharField(max_length=100)

