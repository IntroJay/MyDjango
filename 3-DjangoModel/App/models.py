from django.db import models


# Create your models here.

# 创建人员类
class Person(models.Model):
    p_name = models.CharField(max_length=16)
    p_age = models.IntegerField(default=18)


# 创建人类
class People(models.Model):
    p_name = models.CharField(max_length=16)
    p_register = models.DateTimeField(auto_now=True)


class TeachManager(models.Manager):
    def get_queryset(self):
        # 调用原Manager中get_queryset()进行筛选
        return super(TeachManager, self).get_queryset().filter(is_delete=False)

    def create_grade(self, name, boy_num=23, girl_num=20):
        # 模型是和管理者关联的，关联字段叫model
        grade = self.model()
        grade.g_name = name
        grade.g_boy_num = boy_num
        grade.g_girl_num = girl_num
        return grade


# 创建班级类
class Grade(models.Model):
    g_name = models.CharField(max_length=16)
    g_boy_num = models.IntegerField(default=30)
    g_girl_num = models.IntegerField(default=20)
    is_delete = models.BooleanField(default=False)

    g_objects = models.Manager()
