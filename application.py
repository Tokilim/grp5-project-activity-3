from requests import get
import requests

# Get the current device's public ip address from ipify.org API
ip = get('https://api.ipify.org').text
# API Key from ipstack dashboard
API_KEY = "a3d54c78657ee548ee679b10ec8a36e0"

url = f"http://api.ipstack.com/{ip}?access_key={API_KEY}"
try:
    # Get a request from the API link and store it in a JSON format
    response = requests.get(url)
    data = response.json()

    # Error Handling
    if 'error' in data:
        print(f"Error: {data['error']['info']}")
    else:
        # Acessing information in the JSON and display it
        print("Geolocation Information:")
        print(f"IP Address: {data['ip']}")
        print(f"Country: {data['country_name']}")
        print(f"Region: {data['region_name']}")
        print(f"City: {data['city']}")
        print(f"Latitude: {data['latitude']}")
        print(f"Longitude: {data['longitude']}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")