# Generated by Django 4.1.1 on 2022-10-03 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='CommentText',
            field=models.CharField(default='', max_length=300),
        ),
    ]
