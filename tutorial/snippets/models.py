from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles



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

    class Meta:
        ordering = ['created']
