# Generated by Django 3.1.3 on 2020-11-17 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo_api', '0010_auto_20201117_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='animals',
            field=models.ManyToManyField(related_name='staff', through='zoo_api.AnimalConnection', to='zoo_api.Animal'),
        ),
    ]