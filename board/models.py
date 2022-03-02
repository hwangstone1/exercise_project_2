from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()