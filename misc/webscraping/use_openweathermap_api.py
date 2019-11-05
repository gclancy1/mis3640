import json
import urllib.request
import pprint

APIKEY = 'YOUR_OWN_APIKEY'
city = 'Wellesley'
country_code = 'us'
URL_OPENWEATHERMAP_ = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    with urllib.request.urlopen(url) as response:
        response_text = response.read().decode('utf-8')
        response_data = json.loads(response_text)

    return response_data


def main():
    weather_json = get_json(URL_OPENWEATHERMAP_)
    pprint.pprint(weather_json)


if __name__ == '__main__':
    main()
