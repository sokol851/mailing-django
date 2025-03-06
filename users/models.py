# coding=utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        verbose_name = u"Пользователь"
        verbose_name_plural = u"Пользователи"

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username
