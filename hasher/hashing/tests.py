from django.test import TestCase
from selenium import webdriver

#functional test class
class FunctionalTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_homepage_isup(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('install', self.browser.page_source)

    def tearDown(self):
        #shutdown and close browser
        self.browser.quit()
