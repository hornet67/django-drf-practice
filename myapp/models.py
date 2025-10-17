from django.db import models

# Create your models here.

class Division(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class District(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=100)

    def __str__(self):
        return self.district_name
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name