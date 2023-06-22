from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    expected_salary = models.IntegerField(null=True, blank=True)
    is_searching = models.BooleanField(default=True)


    def __str__(self):
        return self.name
