from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import date

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def days_passed(self):
        today = date.today()
        delta = today - self.created_at
        return delta.days
    