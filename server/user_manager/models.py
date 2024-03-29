from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32, primary_key=True)
    password = models.CharField(max_length=48, null=False)
    nickname = models.CharField(max_length=32, null=False)
    email = models.EmailField(null=False)
    avatar = models.ImageField(null=True)
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return "username:" + self.username + "nickname:" + self.nickname + " email:" + self.email + " isAdmin:" + self.isAdmin
