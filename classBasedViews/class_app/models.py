from django.db import models

# Create your models here.


class School(models.Model):

    name = models.CharField(max_length=256)
    principle = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Student(models.Model):

    first_name = models.CharField(max_length=256)
    age = models.IntegerField()
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.first_name
