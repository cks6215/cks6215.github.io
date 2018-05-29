from django.db import models
from django.utils import timezone
# Create your models here.


class Subject(models.Model):
    subject = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.subject


class SayingPost(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    content = models.TextField(default='-')
    author = models.CharField(max_length=255, blank=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.content