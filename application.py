from requests import get
import requests

ip = get('https://api.ipify.org').text
API_KEY = "a3d54c78657ee548ee679b10ec8a36e0"

url = f"http://api.ipstack.com/{ip}?access_key={API_KEY}"
try:
    response = requests.get(url)
    data = response.json()

    if 'error' in data:
        print(f"Error: {data['error']['info']}")
    else:
        print("Geolocation Information:")
        print(f"IP Address: {data['ip']}")
        print(f"Country: {data['country_name']}")
        print(f"Region: {data['region_name']}")
        print(f"City: {data['city']}")
        print(f"Latitude: {data['latitude']}")
        print(f"Longitude: {data['longitude']}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")