import requests

def get_ip_details():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()

        ip_address = data.get('ip', 'N/A')
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        postal_code = data.get('postal', 'N/A')
        country = data.get('country', 'N/A')

        print(f'IP Address: {ip_address}')
        print(f'City: {city}')
        print(f'Region/Area: {region}')
        print(f'Postal Code: {postal_code}')
        print(f'Country: {country}')

    except Exception as e:
        print(f'Error fetching IP details: {e}')

if __name__ == "__main__":
    get_ip_details()

