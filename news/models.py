from django.db import models
from django.contrib.auth.models import User


class ArticleNew(models.Model):
    author = models.OneToOneField(
            to=User,
            null=True,
            blank=False,
            on_delete=models.CASCADE,
            related_name='article_new_object'
        )
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(null=True, blank=True, default=0)
    likes_users = models.ManyToManyField(
        to=User,
        blank=True,
    )

    def __str__(self):
        return self.title
