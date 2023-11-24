import requests

def shorten_url_tinyurl(long_url):
    url = f'http://tinyurl.com/api-create.php?url={long_url}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Replace this with the actual long URL you want to shorten
long_url = r"https://github.com/teodor1006/Bachelor-thesis"

short_url = shorten_url_tinyurl(long_url)

if short_url:
    print(f'Shortened URL: {short_url}')
else:
    print('Error shortening URL')