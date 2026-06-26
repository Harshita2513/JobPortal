from django.db import models
from django.contrib.auth.models import User
# class Candidate (models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField()
#     phone = models.IntegerField()
#     education = models.CharField()
#     experience = models.IntegerField()
#     resume = models.ImageField(upload_to='Candidate')
#     profile_photo = models.ImageField(upload_to='Candidate')


# user = User.objects.create_user(
#     username=username,
#     email=email,
#     password=password1,
#     first_name=first_name,
#     last_name=last_name
# )
# class User:
#     username = models.CharField(max_length=100)
#     email= models.EmailField(),
#     password = models.IntegerField(),
#     first_name = models.CharField(max_length=50),
#     last_name = models.CharField(max_length=50),

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    

# class Job(models.Model) :
#     title = models.CharField()
#     description = models.TextField()
#     salary = models.IntegerField()
#     location = models.CharField()
#     experience_required = models.IntegerField()
#     company = models.CharField()
#     posted_date = models.DateField()
#     deadline = models.DateTimeField()


# class Application(models.Model) :
#     candidate = models.CharField(max_length=50)
#     job = models.CharField()
#     resume = models.ImageField(upload_to='Application')
#     applied_date = models.DateField()
#     status = models.BooleanField()


