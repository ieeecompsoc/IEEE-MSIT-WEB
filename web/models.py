# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    event_title = models.CharField(max_length=100, verbose_name = 'Title')
    event_description = models.TextField(verbose_name = 'Description')
    image = models.ImageField(upload_to='uploads/events/%Y/%m/%d/', blank=True, null=True)
    create_date = models.DateTimeField(verbose_name = 'Created on:', default = timezone.now)

    def __str__(self):
        return "%s" % (self.event_title)

class Chapter(models.Model):
    chapter = models.CharField(max_length=100, verbose_name="Student Chapter")

    def __str__(self):
        return "%s" % (self.chapter)

class Designation(models.Model):
    designation = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.designation)

class Execom(models.Model):
    name = models.CharField(max_length = 100, verbose_name="Full Name")
    image = models.ImageField(upload_to='uploads/execom/', blank=True, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    facebook = models.URLField(blank=True, null=True)
    linkedIn = models.URLField(blank=True, null=True)

    def __str__(self):
        return "%s" % (self.name)
