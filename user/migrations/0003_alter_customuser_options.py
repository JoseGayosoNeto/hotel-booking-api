# Generated by Django 5.0.6 on 2024-07-26 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_date_of_birthday'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Custom Users'},
        ),
    ]
