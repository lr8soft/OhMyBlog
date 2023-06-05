from django.db import models
from user_manager.models import User


# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(null=False)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True)
    repliesCount = models.IntegerField(default=0)
    pageView = models.IntegerField(default=0)

    def __str__(self):
        return "id:" + self.id + " title:" + self.title + " content:" + self.content + " author:" + self.author + " repliescount:" + self.repliesCount


class Reply(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "id:" + self.id + " article:" + self.article + " author:" + self.author


class Attachments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False)
    file = models.FileField(upload_to='upload')
    md5 = models.TextField(null=False)

    def __str__(self):
        return "id:" + self.id + " name:" + self.name + " md5:" + self.md5