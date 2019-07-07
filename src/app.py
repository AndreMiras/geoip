import os

from flask import request
from flask_api import FlaskAPI
from geolite2 import geolite2

app = FlaskAPI(__name__)


@app.route("/ip/<string:ip>/")
def geoip(ip):
    reader = geolite2.reader()
    geo_info = reader.get(ip)
    geo_info = geo_info or {}
    geo_info.update({'ip': ip})
    geolite2.close()
    return geo_info


@app.route("/")
def index():
    client_ip = request.environ.get(
        'HTTP_X_FORWARDED_FOR', request.remote_addr)
    return geoip(client_ip)


if __name__ == "__main__":
    debug = os.environ.get('REALEASE') is None
    app.run(host='0.0.0.0', debug=debug)
