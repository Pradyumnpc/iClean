# Generated by Django 4.1.1 on 2022-10-17 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shaily',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=300)),
            ],
        ),
    ]