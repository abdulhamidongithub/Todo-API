from django.contrib.auth.models import User
from django.db import models

class Plan(models.Model):
    V = [
        ("Yangi", "Yangi"),
        ("Davom etyapti", "Davom etyapti"),
        ("Bajarilgan", "Bajarilgan"),
    ]
    sarlavha = models.CharField(max_length=30)
    matn = models.TextField(blank=True)
    oxirgi_muddat = models.DateTimeField()
    holat = models.CharField(max_length=20, choices=V)
    def __str__(self):
        return self.sarlavha
