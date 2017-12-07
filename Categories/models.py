# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):

    title = models.CharField(max_length = 255)
    is_deleted = models.BooleanField(default=False)
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

