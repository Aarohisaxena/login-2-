# Generated by Django 4.2.4 on 2023-10-29 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_upload_mri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='mri',
            field=models.ImageField(default='', upload_to='authentication/images'),
        ),
    ]