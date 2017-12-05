from django.db import models
from django import forms
from django.utils import timezone


class ReviewPost(models.Model):

    author = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
