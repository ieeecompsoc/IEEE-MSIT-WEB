# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html
from .models import Event,Chapter,Designation,Execom,Achievment,Sig, Update, SigMentor, Team, Blog, Visitor

class EventAdmin(admin.ModelAdmin):
    list_display=('event_title','event_date','image')
    list_filter=['event_date']

class BlogAdmin(admin.ModelAdmin):
    list_display=('blog_title', 'blog_date', 'image', 'blog_by')
    list_filter=['blog_date']

class ExecomAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        try:
            return format_html('<img src="{}" height="50" width="auto" />'.format(obj.image.url))
        except:
            return None;
    image_tag.short_description = 'Image'
    list_display=('name','image_tag','chapter','designation','page_rank')
    list_filter=['chapter']

class AchievmentAdmin(admin.ModelAdmin):
    list_display=('achievment', 'achievment_date')

# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Execom,ExecomAdmin)
admin.site.register(Chapter)
admin.site.register(Designation)
admin.site.register(Achievment)
admin.site.register(Sig)
admin.site.register(Update)
admin.site.register(SigMentor)
admin.site.register(Team)
admin.site.register(Visitor)

