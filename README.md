# GeoIP

Web API to MaxMind GeoLite2.

## Usage
Request:
```sh
curl https://geoip2.herokuapp.com/ip/8.8.8.8
```
Response:
```json
{
  "continent": {
    "code": "NA",
    "geoname_id": 6255149,
    "names": {
      "de": "Nordamerika",
      "en": "North America",
      "es": "Norteam\u00e9rica",
      "fr": "Am\u00e9rique du Nord",
      "ja": "\u5317\u30a2\u30e1\u30ea\u30ab",
      "pt-BR": "Am\u00e9rica do Norte",
      "ru": "\u0421\u0435\u0432\u0435\u0440\u043d\u0430\u044f \u0410\u043c\u0435\u0440\u0438\u043a\u0430",
      "zh-CN": "\u5317\u7f8e\u6d32"
    }
  },
  "country": {
    "geoname_id": 6252001,
    "iso_code": "US",
    "names": {
      "de": "USA",
      "en": "United States",
      "es": "Estados Unidos",
      "fr": "\u00c9tats-Unis",
      "ja": "\u30a2\u30e1\u30ea\u30ab\u5408\u8846\u56fd",
      "pt-BR": "Estados Unidos",
      "ru": "\u0421\u0428\u0410",
      "zh-CN": "\u7f8e\u56fd"
    }
  },
  "ip": "8.8.8.8",
  "location": {
    "accuracy_radius": 1000,
    "latitude": 37.751,
    "longitude": -97.822
  },
  "registered_country": {
    "geoname_id": 6252001,
    "iso_code": "US",
    "names": {
      "de": "USA",
      "en": "United States",
      "es": "Estados Unidos",
      "fr": "\u00c9tats-Unis",
      "ja": "\u30a2\u30e1\u30ea\u30ab\u5408\u8846\u56fd",
      "pt-BR": "Estados Unidos",
      "ru": "\u0421\u0428\u0410",
      "zh-CN": "\u7f8e\u56fd"
    }
  }
}
```

## Endpoints

### URL: [/](https://geoip2.herokuapp.com/)
The root endpoint returns geo IP info of the client IP.
```sh
curl https://geoip2.herokuapp.com
```

### URL: [/ip/&lt;string:ip&gt;](https://geoip2.herokuapp.com/ip/8.8.8.8)
It's also possible to provide a custom IP via this endpoint.
```sh
curl https://geoip2.herokuapp.com/ip/8.8.8.8
```
Also works with IPv6.
```sh
curl https://geoip2.herokuapp.com/ip/2001:4860:4860::8888
```

## Contribute
This is a fairly simple project, but contributions are welcomed.
Before pull requesting, make sure tests are passing.
```sh
make test
```

## Credits
This product includes GeoLite2 data created by MaxMind, available from
[https://www.maxmind.com](https://www.maxmind.com).
