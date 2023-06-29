from django.db import models
from worker.models import Worker
from worker.models import User

# Create your models here.
class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
    description = models.TextField(default='Нет описания')
    is_relevant = models.BooleanField(default=True)
    email = models.EmailField()
    contacts = models.CharField(max_length=100, verbose_name='Контакты')
    candidate = models.ManyToManyField(
        to=Worker,
        blank=True,
    )

    def __str__(self):
        return self.title

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
    address = models.CharField(max_length=255)
    number_of_employees = models.IntegerField(null=True, blank=True)
    is_hunting = models.BooleanField(default=True)


    def __str__(self):
        return self.name