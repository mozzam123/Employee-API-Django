# models.py

from django.db import models

class Address(models.Model):
    hno = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

class WorkExperience(models.Model):
    companyName = models.CharField(max_length=255)
    fromDate = models.CharField(max_length=255)
    toDate = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Qualification(models.Model):
    qualificationName = models.CharField(max_length=255)
    fromDate = models.CharField(max_length=255)
    toDate = models.CharField(max_length=255)
    percentage = models.FloatField()

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phoneNo = models.CharField(max_length=15, blank=True, null=True)
    addressDetails = models.OneToOneField(Address, on_delete=models.CASCADE)
    workExperience = models.ManyToManyField(WorkExperience)
    qualifications = models.ManyToManyField(Qualification)
    projects = models.ManyToManyField(Project)
    photo = models.CharField(max_length=15, blank=True, null=True)


    def __str__(self) -> str:
        return self.name
