# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PhoneNumber(models.Model):
    abc = models.PositiveIntegerField(
        verbose_name=_('Код (первые три цифры)')
    )

    start_number = models.PositiveIntegerField(
        verbose_name=_('От')
    )

    end_number = models.PositiveIntegerField(
        verbose_name=_('До')
    )


    class Meta:
        verbose_name = _('Диапазон телефонных номеров')
        verbose_name_plural = _('Диапазоны телефонных номеров')

    def __str__(self):
        return f'{self.abc} {self.start_number} {self.end_number}'
