# Generated by Django 4.1.1 on 2022-10-28 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_issue_isresolved'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='isAuthority',
            field=models.BooleanField(default=False),
        ),
    ]