# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DownloadData(models.Model):
    DOWNLOAD_DIRECTORY = 'download/'

    actual_date = models.DateField(
        verbose_name=_('Дата загрузки'), auto_now=True
    )

    abc3 = models.FileField(
        verbose_name=_('Файл ABC-3xx.csv'), upload_to=DOWNLOAD_DIRECTORY,
        blank=True, null=True
    )

    abc4 = models.FileField(
        verbose_name=_('Файл ABC-4xx.csv'), upload_to=DOWNLOAD_DIRECTORY,
        blank=True, null=True
    )

    abc8 = models.FileField(
        verbose_name=_('Файл ABC-8xx.csv'), upload_to=DOWNLOAD_DIRECTORY,
        blank=True, null=True
    )

    def9 = models.FileField(
        verbose_name=_('Файл DEF-9xx.csv'), upload_to=DOWNLOAD_DIRECTORY,
        blank=True, null=True
    )

    class Meta:
        verbose_name = _('Загруженные данные')
        verbose_name_plural = _('Загруженные данные')

    def __str__(self):
        return f'{self.id} {self.actual_date}'
