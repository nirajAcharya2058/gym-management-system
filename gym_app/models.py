from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# from distutils.command.upload import upload
from django.db import models

# Create your models here.
# this file we creates a database tables

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.name

class Enrollment(models.Model):        
    FullName = models.CharField(max_length=25)
    Email = models.EmailField()
    Gender = models.CharField(max_length=25)
    PhoneNumber = models.CharField(max_length=12)
    DOB = models.CharField(max_length=50)
    SelectMembershipplan = models.CharField(max_length=200)
    SelectTrainer = models.CharField(max_length=55)
    Reference = models.CharField(max_length=55)
    Address = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    paymentStatus = models.CharField(max_length=55, blank=True, null=True)
    price = models.IntegerField(max_length=55, blank=True, null=True)
    DueDate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.FullName

class Trainer(models.Model):
    name = models.CharField(max_length=55)
    gender = models.CharField(max_length=25)
    phone = models.CharField(max_length=10)
    salary = models.IntegerField(max_length=25)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

class MembershipPlan(models.Model):
    plan = models.CharField(max_length=185)
    price = models.IntegerField(max_length=55)

    def __int__(self):
        return self.id


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='gallery')
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __int__(self):
        return self.id


class Attendance(models.Model):
    Selectdate = models.DateTimeField(auto_now_add=True)
    phonenumber = models.CharField(max_length=15)
    Login = models.CharField(max_length=200)
    Logout = models.CharField(max_length=200)
    SelectWorkout = models.CharField(max_length=200)
    TrainedBy = models.CharField(max_length=200)

    def __int__(self):
        return self.id


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services')

    def __str__(self):
        return self.title

class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Payment(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.member.username} - {self.amount}"

class Membership(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.member.username} - {self.plan.plan}"

from django.contrib.auth.models import User

class EmailOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)