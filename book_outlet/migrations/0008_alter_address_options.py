# Generated by Django 3.2.5 on 2021-08-05 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0007_rename_addess_author_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address Entries'},
        ),
    ]
