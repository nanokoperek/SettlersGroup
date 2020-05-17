from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

class JobEmployee(models.Model):
    employee = models.ForeignKey(User, on_delete = models.CASCADE)
    place = models.CharField(max_length=200)
    date_start = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    date_end = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    hours_per_day = models.DecimalField(decimal_places=2, max_digits=4)
