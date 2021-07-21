
from django.db import models



class Brand(models.Model):
    class Meta:
        verbose_name = 'Брэнд'

    brand_name = models.CharField(max_length=50)
    country_location = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.brand_name}'


class Instrument(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='instrument')
    model_name = models.CharField(max_length=40, null=True)
    production_year = models.CharField(max_length=20, null=True)
    segment = models.CharField(max_length=40, null=True)
    description = models.TextField()
    features = models.TextField()
    photo = models.ImageField(null=True)
    instrument_type = models.CharField(max_length=50)
    in_stock = models.BooleanField(default=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=500)

# class ContentModerator(AbstractUser):
#     username = models.CharField(max_length=50, unique=True)
#     first_name = models.CharField(max_length=150, blank=True)
#     last_name = models.CharField(max_length=150, blank=True)
#     email = models.EmailField(blank=True)




