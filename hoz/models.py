from django.db import models
from django import forms
from django.utils import timezone


class ReviewPost(models.Model):
    """ @Package         hoz.models
        @About           review and rating
        @Build           1.0
        @Author          riff_spliff
    """

    author = models.CharField(max_length=40)
    text = models.TextField(max_length=180)
    rating = models.IntegerField(default=0)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text


class RequestPost(models.Model):
    """ @Package         hoz.models
        @About           standart order
        @Build           1.0
        @Author          riff_spliff
    """

    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    text = models.TextField(max_length=180)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text


class CallbackPost(models.Model):
    """ @Package         hoz.models
        @About           simple callback order
        @Build           1.0
        @Author          riff_spliff
    """

    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.phone
