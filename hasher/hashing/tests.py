from django.test import TestCase
from selenium import webdriver

#functional test class
# class FunctionalTestCase(TestCase):
#
#     def setUp(self):
#         self.browser = webdriver.Firefox()
#
#     def test_homepage_isup(self):
#         self.browser.get('http://localhost:8000')
#         self.assertIn('Enter hash here:', self.browser.page_source)
#
#     def test_hash_of_hello(self):
#         self.browser.get('http://localhost:8000')
#         self.assertIn('Enter hash here:', self.browser.page_source)
#         #find element on the screen where text can be input
#         text = self.browser.find_element_by_id('id_text')
#         text.send_keys('hello')
#         self.browser.find_element_by_name('submit').click()
#         #result hash should be displayed
#         self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824',
#                       self.browser.page_source)
#
#     def tearDown(self):
#         #shutdown and close browser
#         self.browser.quit()

class UnitTestCase(TestCase):

    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hashing/home.html')
