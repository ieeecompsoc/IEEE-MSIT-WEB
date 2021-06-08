from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class shorturl(models.Model):
    original_url=models.URLField(blank=False, max_length=500)
    short_query=models.CharField(blank=False, max_length=8)
    visits=models.IntegerField(default=0)