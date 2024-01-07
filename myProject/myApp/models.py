from django.db import models
from django.contrib.auth.models import AbstractUser


class Office_User(AbstractUser):
    USER=[
        ('office_manage','Office_Manager'),('administrative_assistant','Administrative_Assistant'),('executive_assistant','Executive_Assistant'),('receptionist','Receptionist')
    ]
    display_name=models.CharField(max_length=100,null=True)
    email=models.EmailField(unique=True,null=True)
    password=models.CharField(max_length=100,null=True)
    confirm_password=models.CharField(max_length=100,null=True)
    job_type = models.CharField(choices=USER,max_length=255,null=True)
    Profile_picture=models.ImageField(upload_to="media/Profile_pic",null=True)

    def __str__(self):
        return self.display_name or "No Display Name"





class Office_Manager_Profile(models.Model):
    user=models.OneToOneField(Office_User, on_delete=models.CASCADE,null=True, related_name='office_manage')

    def __str__(self):
        return self.user.display_name or "No Display Name"
    


class Administrative_Assistant_Profile(models.Model):
    user=models.OneToOneField(Office_User, on_delete=models.CASCADE,null=True, related_name='administrative_assistant')
    resumes=models.FileField(upload_to="media/resumes",null=True)
    skils=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.display_name or "No Display Name"


class Executive_Assistant_Profile(models.Model):
    user=models.OneToOneField(Office_User, on_delete=models.CASCADE,null=True, related_name='executive_assistant')

    def __str__(self):
        return self.user.display_name or "No Display Name"
    


class Receptionist_Profile(models.Model):
    user=models.OneToOneField(Office_User, on_delete=models.CASCADE,null=True, related_name='receptionist')

    def __str__(self):
        return self.user.display_name or "No Display Name"