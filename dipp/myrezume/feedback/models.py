from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тема сообщения')
    author = models.CharField(max_length=255, blank=True, verbose_name='Автор')
    mail = models.CharField(max_length=255, blank=True, verbose_name='e-mail' )
    description = models.TextField(blank=True, verbose_name='Сообщение' )
    # date = models.DateField(verbose_name='Дата',blank=True)
    # alles = models.BooleanField(blank=True, default=True, verbose_name='Показывать всем ' )

    def __str__(self):
        return self.title