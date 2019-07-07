import os

from flask import Flask, jsonify, request
from geolite2 import geolite2

app = Flask(__name__)


@app.route("/ip/<string:ip>/")
def geoip(ip):
    reader = geolite2.reader()
    geo_info = reader.get(ip)
    geo_info = geo_info or {}
    geo_info.update({'ip': ip})
    geolite2.close()
    return jsonify(geo_info)


@app.route("/")
def index():
    return geoip(request.remote_addr)


if __name__ == "__main__":
    debug = os.environ.get('REALEASE') is None
    app.run(host='0.0.0.0', debug=debug)
