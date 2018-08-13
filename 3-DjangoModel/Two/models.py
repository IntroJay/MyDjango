from django.db import models

# Create your models here.

class Game(models.Model):
    g_name = models.CharField(max_length=16)
    g_type = models.IntegerField(default=1)

    def get_type(self):
        return self.g_type