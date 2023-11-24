from django.db import models
# from django.contrib.auth.models import AbstractUser

class AddressDetails(models.Model):
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
    percentage = models.FloatField()

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class UserModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phoneNo = models.CharField(max_length=15, blank=True)
    addressDetails = models.OneToOneField(AddressDetails, on_delete=models.CASCADE, null=True, blank=True)
    workExperience = models.ManyToManyField(WorkExperience)
    qualifications = models.ManyToManyField(Qualification)
    projects = models.ManyToManyField(Project)
    photo = models.TextField(blank=True)  # Assuming Base64 image data is stored as a string

    def __str__(self):
        return self.name
