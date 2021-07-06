from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .views import HomePageView
from django.urls.base import resolve
# Create your tests here.

class HomePageTast(SimpleTestCase):
    
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
    
    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
    
    
    def test_homepage_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)