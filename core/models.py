from django.db import models
from worker.models import Worker
from worker.models import User


# Create your models here.

class Skill(models.Model):

    title = models.CharField(max_length=255)
    type_of_employment = [
        ('full time work', 'полный рабочий день'),
        ('part-time employment', 'частичная занятость'),
        ('piecework', 'сдельная работа'),

    ]
    my_field = models.CharField(
        max_length=20,
        choices=type_of_employment,
        default='full time work',
    )


    def __str__(self):
        return self.title

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
    description = models.TextField(default='Нет описания')
    is_relevant = models.BooleanField(default=True)
    email = models.EmailField()
    contacts = models.CharField(max_length=100, verbose_name='Контакты')
    required_work_experience = models.IntegerField(null=True, blank=True)
    type_of_employment = [
        ('full time work', 'полный рабочий день'),
        ('part-time employment', 'частичная занятость'),
        ('piecework', 'сдельная работа'),

    ]
    employment = models.CharField(
        max_length=20,
        choices=type_of_employment,
        default='full time work',
        verbose_name='Занятость'
    )

    candidate = models.ManyToManyField(
        to=Worker,
        blank=True,
    )
    skills = models.ManyToManyField(
        to=Skill,
        blank=True,
    )


    category = models.ForeignKey(
        to='Category',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name='категория'
    )

    def __str__(self):
        return self.title

class Meta:
    verbose_name = 'Вакансия'
    verbose_name_plural = 'Вакансии'
    ordering = ['salary']


class Category(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    view = models.ManyToManyField(
        to=User,
        blank=True,
    )


class Company(models.Model):
    name = models.CharField(max_length=255)
    founding_date = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    number_of_employees = models.IntegerField(null=True, blank=True)
    is_hunting = models.BooleanField(default=True)

    workers = models.ManyToManyField(
        to=Worker,
        blank=True,
        related_name='company',
    )
    def __str__(self):
        return self.name

