from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField()
    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    year = models.DateField()
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='model')
    def __str__(self):
        return self.name

class Car(models.Model):
    chasis_number = models.CharField(max_length=100, unique=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='car', null=True)
    def __str__(self):
        return self.chasis_number

class Engine(models.Model):
    engine_number = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    horsepower = models.IntegerField()
    torque = models.IntegerField()
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name="engine", null=True, blank=True)
    def __str__(self):
        return self.engine_number

class Features(models.Model):
    feature = models.CharField(max_length=100)
    model = models.ManyToManyField(Model, related_name='features')
    def __str__(self):
        return self.feature
    class Meta():
        verbose_name_plural = 'Features'


class ShowRoom(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    opening = models.DateField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    brands = models.ManyToManyField(Brand, related_name='showroom')
    class Meta():
        verbose_name_plural = 'ShowRooms'
    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female')
    ])
    email = models.EmailField(max_length=100)
    showroom = models.ForeignKey(ShowRoom, on_delete=models.CASCADE, related_name='staff')
    class Meta():
        verbose_name_plural = 'Staff'