from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField(validators=[
        MinValueValidator(-90, "Latitude must be greater than -90."),
        MaxValueValidator(90, "Latitude must be less than 90.")
    ])
    longitude = models.FloatField(validators=[
        MinValueValidator(-180, "Longitude must be greater than -180."),
        MaxValueValidator(180, "Longitude must be less than 180.")
    ])

    def __str__(self) -> str:
        return f"{self.name} at {self.latitude}, {self.longitude}"