# Generated by Django 4.1.2 on 2022-10-31 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
