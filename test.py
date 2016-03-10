from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	def test_login_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertTrue('Please login', response.data)

# Ensure login behaves correctly with corrent credentials
	def test_correct_login(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username="admin", password="admin"),
			follow_redirects=True
			)
		self.assertIn(b'You were just logged in', response.data)

#Ensure log in behaves correctly with incorrect credentials
	def test_incorrect_login(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username="wrong", password="wrong"),
			follow_redirects=True
			)
		self.assertIn(b'Invaild credentials, please try again', response.data)

#Ensure logout behaves correctly
	def test_logout(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username="admin", password="admin"),
			follow_redirects=True
			)
		response = tester.get('/logout', follow_redirects=True)
		self.assertIn('You werer just logged out',response.data)

#Ensure the main page requires login
	def test_main_route_requires_login(self):
		tester = app.test_client(self)
		response = tester.get('/', follow_redirects=True)
		self.assertIn('You need to login first.', response.data)

#Ensure the logout page requires login
	def test_logout_route_requires_login(self):
		tester = app.test_client(self)
		response = tester.get('/logout', follow_redirects=True)
		self.assertIn('You need to login first.', response.data)

#Ensure that posts show up on the main page
	def test_posts_show_up_on_main_page(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username="admin", password="admin"),
			follow_redirects=True
			)
		response = tester.get('/', content_type='html/text')
		self.assertIn('Posts:',response.data)

if __name__ == '__main__':
	unittest.main()