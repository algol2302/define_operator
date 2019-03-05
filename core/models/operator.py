# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Operator(models.Model):
    name = models.CharField(
        verbose_name=_('Название'), max_length=255
    )

    class Meta:
        verbose_name = _('Оператор')
        verbose_name_plural = _('Операторы')

    def __str__(self):
        return f'{self.id} {self.name}'
