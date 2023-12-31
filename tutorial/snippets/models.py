from django.db import models
from django.contrib.auth.models import User

def user():
    return User.objects.get_or_create(pk=1,username="m")

class Snippet(models.Model):

    class Lang(models.TextChoices):
        PYTHON = 'py', 'Python'
        JAVA = 'javac', 'Java'
        C_PLUS_PLUS = 'cpp', 'C++'
        C_SHARP = 'csharp', 'C#'

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    usable = models.BooleanField(default=False)
    language = models.CharField(choices=Lang.choices, max_length=100,default=Lang.PYTHON)
    owner = models.ForeignKey(User, related_name='snippets', on_delete=models.CASCADE,default=user()[0].pk)


    class Meta:
        ordering = ['created']

