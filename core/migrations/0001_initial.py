# Generated by Django 4.2.2 on 2023-06-30 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('worker', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.TextField(blank=True, null=True)),
                ('view', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('number_of_employees', models.IntegerField(blank=True, null=True)),
                ('is_hunting', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(default='Нет описания')),
                ('is_relevant', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254)),
                ('contacts', models.CharField(max_length=100, verbose_name='Контакты')),
                ('candidate', models.ManyToManyField(blank=True, to='worker.worker')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.category', verbose_name='категория')),
            ],
        ),
    ]
