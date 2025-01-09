from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}

NOT_NULLABLE = {'blank': False, 'null': False}


class User(AbstractUser):
    muster_mode = models.BooleanField(default=False, verbose_name='Режим поверки')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
