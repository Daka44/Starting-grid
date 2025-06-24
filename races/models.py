from django.db import models

# Create your models here.
class Race(models.Model):
    nation = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    circuit_info = models.TextField(default="정보없음")

    def __str__(self):
        return f"{self.nation} {self.date}"