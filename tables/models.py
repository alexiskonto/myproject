from django.db import models
from django.contrib.auth.models import User

class TableEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Each user has their own data
    name = models.CharField(max_length=255)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.value} (User: {self.user.username})"
