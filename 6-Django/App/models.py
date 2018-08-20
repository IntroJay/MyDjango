from django.db import models


# Create your models here.
# 用户模型
class UserModel(models.Model):
    u_name = models.CharField(max_length=16, unique=True)
    u_password = models.CharField(max_length=18)
    u_token = models.CharField(max_length=128, unique=True)


# 头像上传模型
class BuyerModel(models.Model):
    b_name = models.CharField(max_length=16)
    # 相对于Django的媒体中心 MEDIA_ROOT
    b_icon = models.ImageField(upload_to='icons')
