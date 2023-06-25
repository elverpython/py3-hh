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
    view = models.ManyToManyField(
        to=User,
        blank=True,
    )

    def __str__(self):
        return self.title

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    number_of_employees = models.IntegerField(null=True, blank=True)
    is_hunting = models.BooleanField(default=True)


    def __str__(self):
        return self.name
