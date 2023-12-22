from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=25)
    password=models.CharField(max_length=15)
    RADIO_CHOICES = [
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('Not_specified','NOT_SPECIFIED')
    ]
    gender=models.CharField(max_length=20,choices=RADIO_CHOICES, default='Not_specified')
    def __str__(self):
        return self.name

class admin_log(models.Model):
    admin_name=models.CharField(max_length=25)
    admin_pass=models.CharField(max_length=20)
    def __str__(self):
        return self.admin_name

class user_log(models.Model):
    full_name=models.CharField(max_length=25)
    phone=models.IntegerField()
    gmail=models.CharField(max_length=25)
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    RADIO_CHOICES = [
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('Not_specified', 'NOT_SPECIFIED')
    ]
    gender = models.CharField(max_length=20, choices=RADIO_CHOICES, default='Not_specified')
    def __str__(self):
        return self.full_name

class doctor_form(models.Model):
    doctor_name=models.CharField(max_length=25)
    doctor_id=models.IntegerField()
    doctor_img=models.FileField()
    doctor_dept=models.CharField(max_length=30)
    def __str__(self):
        return self.doctor_name

class appoint_booking(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    date=models.CharField(max_length=25)
    phone=models.IntegerField()
    department=models.CharField(max_length=25)
    message=models.CharField(max_length=2000)
    payment_id=models.CharField(max_length=10)
    RADIO_CHOICES = [
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('Not_specified', 'NOT_SPECIFIED')
    ]
    gender = models.CharField(max_length=20, choices=RADIO_CHOICES, default='Not_specified')
    status_choice = [
        ('approve', 'approve'),
        ('reject', 'reject'),
        ('pending','pending')
    ]
    status = models.CharField(max_length=10, choices=status_choice, default='pending')
    def __str__(self):
        return self.name
