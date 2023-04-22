from django.db import models

# Create your models here.

class MyUser(models.Model):

    user_name = models.CharField('Username', max_length=50)
    user_password = models.CharField('Password', max_length=16)

    def __str__(self):
        return self.user_name
    
