from django.test import TestCase, Client

# Create your tests here.

class CurrencyApiTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create test data if necessary

    def test_currency_get_request_without_parameters(self):
        response = self.client.get('/currency/')
        self.assertEqual(response.status_code, 200)
        # Add more assertions for response content

    def test_currency_get_request_with_valid_name_parameter(self):
        response = self.client.get('/currency/?name=USD&sort=valueAsc')
        self.assertEqual(response.status_code, 200)
        # Add more assertions for response content

    def test_currency_get_request_with_invalid_name_parameter(self):
        response = self.client.get('/currency/?name=invalid_name')
        self.assertEqual(response.status_code, 200)
        # Add more assertions for response content

    def test_currency_invalid_request(self):
        response = self.client.post('/currency/')
        self.assertEqual(response.status_code, 400)