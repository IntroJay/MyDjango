from django.db import models


# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=16)


class Grade(models.Model):
    g_name = models.CharField(max_length=16)


class Learn(models.Model):
    l_name = models.CharField(max_length=16)


class UserModel(models.Model):
    u_name = models.CharField(max_length=16, unique=True)
    u_token = models.CharField(max_length=64, unique=True)
    u_password = models.CharField(max_length=18)
