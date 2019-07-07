import unittest

from flask_api import status

from app import app


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_index(self):
        response = self.client.get('/')
        assert response.status_code == status.HTTP_200_OK
        assert response.json == {'ip': '127.0.0.1'}

    def test_geoip(self):
        response = self.client.get('/ip/8.8.8.8')
        assert response.status_code == status.HTTP_200_OK
        assert response.json.keys() == {
            'continent', 'country', 'location', 'registered_country', 'ip'
        }
