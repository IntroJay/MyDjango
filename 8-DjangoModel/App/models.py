from django.db import models


# Create your models here.
# 添加人类
class Person(models.Model):
    p_name = models.CharField(max_length=16)


# 添加身份证类
class IDCard(models.Model):
    id_num = models.CharField(max_length=20)
    # on_delete=models.PROTECT 安全保护
    id_person = models.OneToOneField(Person, on_delete=models.PROTECT)


# 添加班级类
class Grade(models.Model):
    g_name = models.CharField(max_length=16)


# 添加学生类
class Student(models.Model):
    s_name = models.CharField(max_length=16)
    #
    s_grade = models.ForeignKey(Grade, on_delete=models.SET_DEFAULT, null=True, default=1)


# 添加买手类
class Buyer(models.Model):
    b_name = models.CharField(max_length=16)


# 添加商品类
class Goods(models.Model):
    g_name = models.CharField(max_length=32)

    g_buyer = models.ManyToManyField(Buyer)


# 添加动物类
class Anmial(models.Model):
    a_name = models.CharField(max_length=16)

    # 将属性传给子类储存
    class Meta:
        abstract = True


# 添加狗类并继承动物类
class Dog(Anmial):
    d_legs = models.IntegerField(default=4)


# 添加鱼类并继承动物类
class Fish(Anmial):
    f_env = models.CharField(max_length=32)
