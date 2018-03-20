# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class firstmodel(models.Model):
    text_field=models.CharField(max_length=200, default='record entered')