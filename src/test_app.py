import unittest

from flask_api import status

from app import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_index(self):
        """
        Index endpoint returns client IP info.
        Note there's no geo IP info for this address.
        """
        response = self.client.get('/')
        assert response.status_code == status.HTTP_200_OK
        assert response.json == {'ip': '127.0.0.1'}

    def test_index_remote_addr(self):
        """
        Checks the client IP is being picked up on the index.
        """
        ip_address = '1.2.3.4'
        environ_base = {
            'REMOTE_ADDR': ip_address,
        }
        response = self.client.get('/', environ_base=environ_base)
        assert response.status_code == status.HTTP_200_OK
        assert response.json['ip'] == ip_address

    def test_index_x_forwarded_for(self):
        """
        Checks the `HTTP_X_FORWARDED_FOR` header is used when available.
        """
        ip_address = '4.3.2.1'
        environ_base = {
            'HTTP_X_FORWARDED_FOR': ip_address,
        }
        response = self.client.get('/', environ_base=environ_base)
        assert response.status_code == status.HTTP_200_OK
        assert response.json['ip'] == ip_address

    def test_geoip(self):
        response = self.client.get('/ip/8.8.8.8')
        assert response.status_code == status.HTTP_200_OK
        assert response.json.keys() == {
            'continent', 'country', 'location', 'registered_country', 'ip'
        }
