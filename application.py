from requests import get
import requests,json

# Get the current device's public ip address from ipify.org API
ip = get('https://api.ipify.org').text
# API Key from ipstack dashboard
API_KEY = "a3d54c78657ee548ee679b10ec8a36e0"

url = f"http://api.ipstack.com/{ip}?access_key={API_KEY}"
url2 = f"http://ip-api.com/json/{ip}?fields=timezone,currency,as,isp" #2nd Api

try:
    # Get a request from the API link and store it in a JSON format
    response = requests.get(url)
    data = response.json()
    response2 = requests.get(url2)
    data2 = response2.json()
    # Replace 'YOUR_COUNTRY_CODE' with the country code for the desired country (e.g., 'USD' for the United States)
    country_code = data['country_code']

    # Make the API request to fetch currency data
    url3 = f"https://restcountries.com/v3/alpha/{country_code}" #3rd Api

    response3 = requests.get(url3)
    data3 = response3.json()

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
        # new Features From Backlog
        print("Timezone:", data2["timezone"])
        print("Currency:", data2["currency"])
        if response3.status_code == 200:
            data3 = response3.json()
            # pretty_json = json.dumps(data3, indent=4)
            # print(pretty_json)
            if data3:
                currencies = data3[0].get('currencies', [])                
                if currencies:
                    php_name = currencies['PHP']['name']
                    php_symbol = currencies['PHP']['symbol']

                    print(f"Name of Currency: {php_name}")
                    print(f"Symbol of Currency: {php_symbol}")
                else:
                    print("Currency data not found for the specified country code.")
            else:
                print("Country data not found for the specified country code.")
        else:
            print("Error: Unable to fetch data.")
        print("ASN (Autonomous System Number):", data2["as"])
        print("Service Provider:", data2["isp"])
        
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

