# Generated by Django 4.2 on 2023-08-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitmentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
