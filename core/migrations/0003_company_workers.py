# Generated by Django 4.2.2 on 2023-07-18 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_resume_profile_photo'),
        ('core', '0002_company_founding_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='workers',
            field=models.ManyToManyField(blank=True, related_name='company', to='worker.worker'),
        ),
    ]