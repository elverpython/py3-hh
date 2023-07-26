# Generated by Django 4.2.2 on 2023-07-24 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_vacancy_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='my_field',
            field=models.CharField(choices=[('full time work', 'полный рабочий день'), ('part-time employment', 'частичная занятость'), ('piecework', 'сдельная работа')], default='full time work', max_length=20),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='required_work_experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
