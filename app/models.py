from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    TYPE_CHOICE =[
        ('V', 'Video'),
        ('B', 'Book'),
        ('EB', 'Ebook'),
        ('T', 'Tutorial'),
    ]
    STATUS_CHOICE = [
        ('D', 'Done'),
        ('P', 'Pending'),
        ('IP', 'In progress'),
    ]
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    duration_time = models.CharField(max_length=30, null=True, blank=True)
    units = models.IntegerField(null=True, blank=True)
    units_done = models.IntegerField(null=True, blank=True)
    type_course = models.CharField(max_length=2, choices=TYPE_CHOICE, null=False, blank=False)
    status_course = models.CharField(max_length=2, choices=STATUS_CHOICE, null=False, blank=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
