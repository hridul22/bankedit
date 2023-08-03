from django.db import models

class District(models.Model):
    name = models.CharField(max_length=100)
    wikipedia_link = models.URLField()

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Reginfo(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    cpass = models.CharField(max_length=100)

    def __str__(self):
        return self.username