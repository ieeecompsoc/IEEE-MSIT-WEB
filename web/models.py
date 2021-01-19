# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Update(models.Model):
    content = models.CharField(max_length=300, verbose_name='Latest News')
    create_date = models.DateTimeField(verbose_name = 'Created on:', default = timezone.now)

    def __str__(self):
        return "%s" % (self.content)

class Event(models.Model):
    event_title = models.CharField(max_length=100, verbose_name = 'Title')
    event_description = models.TextField(verbose_name = 'Description')
    image = models.ImageField(upload_to='events/', blank=False, null=True)
    report = models.FileField(upload_to='events/', null=True, blank=True)
    register_url = models.URLField(max_length=100, verbose_name='Register Url', blank=True)
    event_date = models.DateTimeField(verbose_name = 'Created on:', default = timezone.now)

    def __str__(self):
        return "%s" % (self.event_title)

class Blog(models.Model):
    blog_title = models.CharField(max_length=100, verbose_name = 'Title')
    blog_content = models.TextField(verbose_name = 'Content')
    image = models.ImageField(upload_to='blogs/', blank=False, null=True)
    blog_date = models.DateTimeField(verbose_name= 'Created on:', default= timezone.now)
    blog_by = models.CharField(max_length=100, verbose_name='Written By:')
    htmlData = models.TextField(help_text="HTML data to be executed as is.",blank=True)

    def __str__(self):
        return "%s" % (self.blog_title)

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
    image = models.ImageField(upload_to='execom/', blank=True, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    facebook = models.URLField(blank=True, null=True)
    linkedIn = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    resume = models.FileField(upload_to='execom/', blank=True, null=True)
    create_date = models.DateTimeField(verbose_name = 'Created on:', default = timezone.now)
    page_rank = models.DecimalField(max_digits=2, decimal_places=0,verbose_name="Frontend Rank",blank=False,default=1)

    def __str__(self):
        return "%s" % (self.name)

class Achievment(models.Model):
    achievment = RichTextField(verbose_name='Achievment')
    achievment_date = models.DateTimeField(verbose_name = 'Achievment Date', default = timezone.now)

    def __str__(self):
        return "%s"  % (self.achievment)

class SigMentor(models.Model):
    name = models.CharField(max_length = 100, verbose_name="Full Name")
    contact = models.CharField(max_length = 13, verbose_name="Mobile Number")
    # sig = models.ForeignKey(Sig,on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.name)

class Sig(models.Model):
    title = models.CharField(max_length=100, verbose_name="SIG Name")
    sig_description = models.TextField(verbose_name='Sig Description', blank=False, null=True)
    image = models.ImageField(upload_to='sigs/', blank=False, null=True)
    timings = models.CharField(max_length = 50, verbose_name="Timings of SIG", blank=False, null=True)
    members = models.ManyToManyField(SigMentor)

    def __str__(self):
        return "%s" % (self.title)

class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    linkedIn = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    resume = models.FileField(upload_to='team/', blank=True, null=True)

    def __str__(self):
        return "%s" % (self.name)
