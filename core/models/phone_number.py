# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .operator import Operator
from .region import Region


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

    operator = models.ForeignKey(
        verbose_name=_('Оператор'), to=Operator,
        on_delete=models.CASCADE, blank=True, null=True
    )

    region = models.ForeignKey(
        verbose_name=_('Регион'), to=Region,
        on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        verbose_name = _('Диапазон телефонных номеров')
        verbose_name_plural = _('Диапазоны телефонных номеров')

    def __str__(self):
        return f'{self.abc} {self.start_number} {self.end_number}'
