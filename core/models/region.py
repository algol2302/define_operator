# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Region(models.Model):
    parent = models.CharField(
        verbose_name=_('Вышестоящий субъект'), max_length=255,
        blank=True, null=True
    )

    name = models.CharField(
        verbose_name=_('Регион'), max_length=255
    )

    class Meta:
        verbose_name = _('Регион')
        verbose_name_plural = _('Регионы')

    def __str__(self):
        return f'{self.id} {self.parent} {self.name}'
