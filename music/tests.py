# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Songs
from .serializers import SongsSerializer


class BaseViewTestCase(APITestCase):
    client = APIClient()

    def setUp(self):
        self.create_song("like glue", "sean paul")
        self.create_song("simple song", "konshens")
        self.create_song("love is wicked", "brick and lace")
        self.create_song("jam rock", "damien marley")

    @staticmethod
    def create_song(title='', artist=''):
        if title and artist:
            Songs.objects.create(title=title, artist=artist)


class GetAllSongsTestCase(BaseViewTestCase):
    def test_get_all_songs(self):
        response = self.client.get(reverse('songs-all', kwargs={"version": "v1"}))

        expected = Songs.objects.all()
        serialised = SongsSerializer(expected, many=True)
        self.assertEqual(response.data, serialised.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
