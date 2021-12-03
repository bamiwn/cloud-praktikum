from app import app
import unittest

class FlaskappTests(unittest.TestCase):
      def setUp(self):
          #create a test client
          self.app = app.test_client()
          #propagate the exceptions to the test client
          self.app.testing = True

      def test_users_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/api/v1/users')
        print (result)
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

      def test_tweets_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/api/v2/tweets')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

      def test_tweets_status_code(self):
        # sends HTTP GET request to the application
        result = self.app.get('/api/v1/info')
        # assert the status code of the reponse
        self.assertEqual(result.status_code, 200)

      def test_addusers_status_code(self):
        # sends HTTP POST request to the application
        result = self.app.post('/api/v1/users', data='{"username":"manish21", "emailid":"manishtest@gmail.com", "password":"test123456","full_name":"manish Kurniawan"}', content_type='application/json')
        print (result)
        #assert the status code of the response
        self.assertEquals(result.status_code, 201)

      def test_updusers_status_code(self):
        #sends HTTP PUT request to the application
        #on the specified path
        result = self.app.put('/api/v1/users/2', data='{"password":"testing123"}', content_type='application/json')
        # assert the status code of the response
        self.assertEquals(result.status_code,200)

      def test_addtweets_status_code(self):
        # sends HTTP GEt request to the application 
        # on the specified path
        result = self.app.post('/api/v2/tweets', data='{"username":"mahesh@rocks", "body":"Wow! is it working testing"}', content_type='application/json')
        # assert the status code of the response
        self.assertEqual(result.status_code, 201)

      def rest_delusers_status_code(self):
        #sends HTTP Delete request to the application
        result = self.app.delete('/api/v1/users', data='{"username":"manish21"}',content_type='application/json')
        #assert the status code of the response
        self.assertEquals(result.status_code, 200)