from django.db import models

from users.models import NULLABLE


class Fluke(models.Model):
    serial_number = models.IntegerField(verbose_name='S/N', unique=True)
    IP = models.CharField(max_length=15, verbose_name='IP')

    def __str__(self):
        return f'{self.serial_number}'

    class Meta:
        verbose_name = 'Эталон'
        verbose_name_plural = 'Эталоны'


class Charm(models.Model):
    serial_number = models.IntegerField(verbose_name='S/N', unique=True)
    calibrator = models.ForeignKey('charm.Fluke', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Калибратор')

    def __str__(self):
        return f'{self.serial_number}'

    class Meta:
        verbose_name = 'Чарм'
        verbose_name_plural = 'Чармы'
