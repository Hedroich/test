# Generated by Django 4.2.5 on 2023-10-20 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sig', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
