# Generated by Django 4.2.2 on 2023-07-14 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photo/', verbose_name='Фото сотрудника'),
        ),
    ]
