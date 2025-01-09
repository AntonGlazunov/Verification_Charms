from django.db import models

from users.models import NULLABLE, NOT_NULLABLE


class Fluke(models.Model):
    serial_number = models.CharField(max_length=100, verbose_name='S/N', unique=True, **NOT_NULLABLE)
    IP = models.GenericIPAddressField(unpack_ipv4=True, verbose_name='IP', **NOT_NULLABLE, help_text='IP адрес устройства')

    def __str__(self):
        return f'{self.serial_number}'

    class Meta:
        verbose_name = 'Эталон'
        verbose_name_plural = 'Эталоны'


class Charm(models.Model):
    serial_number = models.CharField(max_length=100, verbose_name='S/N', unique=True, **NOT_NULLABLE)

    def __str__(self):
        return f'{self.serial_number}'

    class Meta:
        verbose_name = 'Чарм'
        verbose_name_plural = 'Чармы'


class Muster(models.Model):
    measurement = models.DecimalField(max_digits=6, decimal_places=0, **NULLABLE, verbose_name='Результат измерения')
    verifier = models.ForeignKey('users.User', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Поверитель')
    fluke = models.ForeignKey('charm.Fluke', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Fluke')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения', **NULLABLE)
    charm = models.ForeignKey('charm.Charm', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Чарм')

    def __str__(self):
        return f'{self.charm}'

    class Meta:
        verbose_name = 'Поверка'
        verbose_name_plural = 'Поверка'

