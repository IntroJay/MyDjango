from django.db import models


# Create your models here.
# 定义班级
class Grade(models.Model):
    g_name = models.CharField(max_length=16)
    g_info = models.CharField(max_length=64)


# 定义学生
class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=18)
    is_delete = models.BooleanField(default=False)
    s_grade = models.ForeignKey(Grade)


# 定义老师
class Teacher(models.Model):
    t_name = models.CharField(max_length=16)
    t_age = models.IntegerField(default=18)
    t_hobby = models.CharField(max_length=128, null=True)

    class Meta:
        # 给对应的表起个别名
        db_table = 'laoshi'
        # 对结果进行排序
        # ordering = ("t_age",)
