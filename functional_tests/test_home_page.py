from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time


class FunctionalTests(StaticLiveServerTestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
	
	def tearDown(self):
		self.browser.quit()
	
	def test_home_page(self):
		
		# jack goes to the homepage
		self.browser.get(self.live_server_url)
		
		# he sees a big 'Home Page' header
		time.sleep(5)
		self.assertIn('Home Page', self.browser.title)
		
		# he goes to the about page and sees the about page
		# which has a 'About Page' header
		self.browser.find_element_by_link_text('about').click()
		time.sleep(5)
		header = self.browser.find_element_by_tag_name('h1').text
		self.assertEqual(header, 'About Page')
		
		self.fail('End the test!')
