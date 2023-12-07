# Make an account here: https://app.freecurrencyapi.com and copy the API_KEY
# pip install requests (for Windows) / pip3 install requests(for Linux, MacOS)
import requests

API_KEY = 'fca_live_kADN3KqcuLruXq0Ie2yrlLctg4X9jiIZFv04YtKJ'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["BGN", "USD", "CAD", "EUR", "CHF", "GBP", "AUD", "CNY"]

def get_currency_data(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()["data"]
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def convert_amount(amount, base_rate, data):
    print(f"\nConverting {amount} {base} to:")
    for ticker, rate in data.items():
        converted_amount = amount * rate / base_rate
        print(f"{ticker}: {converted_amount:.2f}")

def converter(base, amount):
    data = get_currency_data(base)
    
    if not data or base not in data:
        print("Invalid currency. Please try again!")
        return None

    base_rate = data[base]
    del data[base]

    convert_amount(amount, base_rate, data)
    
    return data

while True:
    base = input("Enter the base currency (or 'Q' to quit): ").upper()

    if base == "Q":
        break 

    amount = float(input(f"Enter the amount in {base}: "))

    data = converter(base, amount)
    if not data:
        continue

    


