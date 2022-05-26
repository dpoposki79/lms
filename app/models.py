from django.db import models
from datetime import timedelta
from django.utils.timezone import now

# Create your models here.

class Courses(models.Model):
    Course_name = models.CharField(max_length=50) 
    Course_language = models.CharField(max_length=50)
    Course_lenght_days = models.DurationField
    start_date = models.DateTimeField(null=True, blank=True)
    Course_price = models.FloatField()
    Course_recordings = models.FileField(null=True, blank=True)

class Instructors(models.Model):
    Ime = models.CharField(max_length=50) 
    Prezime = models.CharField(max_length=50) 
    Email = models.CharField(max_length=50) 
    Course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)

class Students(models.Model):
    Ime = models.CharField(max_length=50) 
    Prezime = models.CharField(max_length=50)
    Adresa = models.CharField(max_length=50) 
    Telefon = models.CharField(max_length=50) 
    Email = models.CharField(max_length=50) 
    Course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)
    Prisustvo = models.BooleanField()
    Comment = models.TextField()
    Homework = models.FileField(null=True, blank=True)
 
 
class Trainings(models.Model):
    Student= models.ForeignKey(Students, on_delete=models.CASCADE, null=True, blank=True)
    Instructor = models.ForeignKey(Instructors, on_delete=models.CASCADE, null=True, blank=True)
    Course= models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)
