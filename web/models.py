# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    event_title = models.CharField(max_length=100, verbose_name = 'Title')
    event_description = models.TextField(verbose_name = 'Description')
    image = models.ImageField(upload_to='%Y/%m/%d/', blank=True, null=True)
    create_date = models.DateTimeField(verbose_name = 'Created on:', default = timezone.now)

    def __str__(self):
        return "%s" % (self.event_title)
