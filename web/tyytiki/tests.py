from django.test import TestCase
from django.urls import resolve
from tyytiki.views import index
from django.http import HttpRequest


class HomePageTest(TestCase):
    def test_root_url(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page(self):
        request = HttpRequest()
        response = index(request)

        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertIn('<title>Главная страница</title>', html)
        self.assertTrue(html.endswith('</html>'))
