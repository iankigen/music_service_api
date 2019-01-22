# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets

from .serializers import SongsSerializer, Songs


class SongsViewSets(viewsets.ModelViewSet):
    serializer_class = SongsSerializer
    queryset = Songs.objects.all()
