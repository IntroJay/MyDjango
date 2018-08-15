from django.db import models


# Create your models here.

# 创建班级类
class Grade(models.Model):
    s_name = models.CharField(max_length=16)


# 创建学生类
class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=18)
    # 外键关联
    s_grade = models.ForeignKey(Grade)
