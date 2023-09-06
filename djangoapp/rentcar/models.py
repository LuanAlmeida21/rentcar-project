from django.db import models

# Create your models here.


class Car(models.Model):

    class Meta:
        verbose_name = 'Cars'
        verbose_name_plural = 'Car'

    make = models.CharField(max_length=40)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    type = models.CharField(max_length=60)
    rent_rate_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    mileage = models.IntegerField()
    car_image = models.ImageField(upload_to='cars/%Y/%m',
                                  blank=False, default=None)

    def __str__(self):
        return self.model
