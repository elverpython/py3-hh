# Generated by Django 4.2.3 on 2023-08-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_vacancy_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='required_work_experience',
            field=models.IntegerField(blank=True, null=True, verbose_name='Необходимый опыт работы'),
        ),
    ]