# Generated by Django 3.2.8 on 2021-11-09 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FLOWER', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
