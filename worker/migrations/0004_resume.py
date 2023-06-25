# Generated by Django 4.2.2 on 2023-06-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('specialization', models.CharField(max_length=255)),
                ('is_relevant', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254)),
                ('contacts', models.CharField(max_length=100, verbose_name='Контакты')),
                ('candidate', models.ManyToManyField(blank=True, to='worker.worker')),
            ],
        ),
    ]
