from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=20)
    taste = models.CharField(max_length=30)

    def __str__(self):
        return self.name