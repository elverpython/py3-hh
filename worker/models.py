from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Worker(models.Model):
    user = models.OneToOneField(
        to=User,
        null=True,
        blank=False,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    expected_salary = models.IntegerField(null=True, blank=True)
    is_searching = models.BooleanField(default=True)


    def __str__(self):
        return self.name

class Comment(models.Model):

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    worker = models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.autor.username

class Resume(models.Model):
    worker = models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE,
        related_name='resume',
    )
    title = models.CharField(max_length=55)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    profile_photo = models.ImageField(
        null=True, blank=True,
        upload_to="profile_photo/",
        verbose_name="Фото сотрудника"
    )
    def __str__(self):
        return self.title
