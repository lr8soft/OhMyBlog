# Generated by Django 4.1 on 2023-06-05 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_manager', '0002_user_isadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('repliesCount', models.IntegerField(default=0)),
                ('pageView', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_manager.user')),
            ],
        ),
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('file', models.FileField(upload_to='upload')),
                ('md5', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('floor', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_manager.user')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article_manager.article')),
            ],
        ),
    ]
