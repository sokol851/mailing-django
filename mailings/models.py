# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from users.models import User

TRUE_FALSE = {'blank': True, 'null': False}
FALSE_FALSE = {'blank': False, 'null': False}
FALSE_TRUE = {'blank': False, 'null': True}


class Message(models.Model):
    theme = models.TextField(max_length=50,
                             verbose_name='Тема письма'
                             )
    body = models.TextField(verbose_name="Сообщение"
                            )
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              verbose_name='Владелец',
                              **TRUE_FALSE
                              )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __unicode__(self):
        return u'{}'.format(self.theme)

    def __str__(self):
        return '{}'.format(self.theme).encode('utf-8')


class Client(models.Model):
    email = models.EmailField(unique=True,
                              verbose_name='Почта клиента'
                              )
    first_name = models.CharField(max_length=50,
                                  default='Не указано',
                                  verbose_name='Имя',
                                  **FALSE_FALSE
                                  )
    last_name = models.CharField(max_length=50,
                                 default='Не указано',
                                 verbose_name='Фамилия',
                                 **FALSE_FALSE
                                 )
    patronymic = models.CharField(max_length=50,
                                  default='Не указано',
                                  verbose_name='Отчество',
                                  **FALSE_TRUE
                                  )
    date_of_birth = models.DateField(verbose_name='День рождения',
                                     **FALSE_FALSE
                                     )
    comment = models.CharField(max_length=50,
                               default='Не указано',
                               verbose_name='Комментарий',
                               **FALSE_TRUE
                               )
    creator = models.ForeignKey(User,
                                max_length=5,
                                on_delete=models.CASCADE,
                                verbose_name='Создатель',
                                **FALSE_TRUE
                                )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __unicode__(self):
        return u'{}'.format(self.email)

    def __str__(self):
        return '{}'.format(self.email).encode('utf-8')
