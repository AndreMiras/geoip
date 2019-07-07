import unittest

from flask_api import status

from app import app


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_root(self):
        response = self.client.get('/')
        assert response.status_code == status.HTTP_200_OK
        assert response.json == {'ip': '127.0.0.1'}
