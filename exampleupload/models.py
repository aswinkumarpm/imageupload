# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class FileUpload(models.Model):
    photo = models.ImageField(upload_to='pic_folder')


class Ads(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField()
    subject = models.TextField()
    photo = models.ImageField(upload_to='ads', blank=True, null=True)
    video = models.FileField(upload_to='videos', blank=True, null=True)

    def _str_(self):
        return self.name
