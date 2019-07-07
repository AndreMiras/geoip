# GeoIP

Web API to MaxMind GeoLite2.

## Usage
Request:
```sh
curl https://geoip2.herokuapp.com/ip/8.8.8.8/
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
