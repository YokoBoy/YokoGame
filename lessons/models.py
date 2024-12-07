from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone

class Lesson(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Убедитесь, что ID 1 существует
    video_url = models.URLField(default='')

class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text


class UserName(models.Model):
    userName = models.CharField(max_length=100)
    userPassword = models.CharField(max_length=30)
    userEmail = models.CharField(max_length=50)
    userAbout = models.TextField(blank=True) # не обязательно заполнять
    userTimeCreat = models.DateTimeField(auto_now_add=True)