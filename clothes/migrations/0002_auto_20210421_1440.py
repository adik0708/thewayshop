# Generated by Django 3.2 on 2021-04-21 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dish',
            new_name='Shirt',
        ),
        migrations.AlterModelOptions(
            name='shirt',
            options={'verbose_name_plural': 'Shirts'},
        ),
    ]
