# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Songs(models.Model):
    title = models.CharField(max_length=255, null=False)
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return 'Song: {} - {}'.format(self.title, self.artist)
