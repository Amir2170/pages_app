from django.test import TestCase


class HomePageViewTest(TestCase):
	
	def test_home_page_view_uses_the_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')
		
	def test_about_page_view_return_correct_template(self):
		response = self.client.get('/about/')
		self.assertTemplateUsed(response, 'about.html')
