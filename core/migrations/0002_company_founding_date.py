# Generated by Django 4.2.2 on 2023-07-06 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='founding_date',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]