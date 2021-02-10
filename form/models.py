from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField("Name", max_length=240)
    birthDate = models.CharField("Birth Date", max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    photo = models.ImageField(blank=True)
    startTime = models.TimeField()
    endTime = models.TimeField()

    def __str__(self):
        return self.name