# Generated by Django 3.2.7 on 2021-11-05 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FLOWER', '0010_alter_flower_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='flower',
            unique_together={('user',)},
        ),
    ]
