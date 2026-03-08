from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    branch = models.CharField(max_length=100)
    cgpa = models.FloatField()
    skills = models.TextField()
    backlog = models.IntegerField()

    def __str__(self):
        return self.user.username