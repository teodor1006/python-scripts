import requests

def get_crypto_price(coin):
    try:
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd'
        response = requests.get(url)
        data = response.json()
        if coin in data and 'usd' in data[coin]:
            return data[coin]['usd']
        else:
            return f"Price not found for {coin}"

    except requests.RequestException as e:
        return f"Error fetching data: {e}"

if __name__ == '__main__':
  coin_name = 'bitcoin'
  price = get_crypto_price(coin_name)
  print(f'{coin_name.capitalize()} Price: {price}')


