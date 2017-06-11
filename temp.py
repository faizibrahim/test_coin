import requests

base_url = 'http://maps.googleapis.com/maps/api/geocode/json'
base_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
my_params = {'address': '15949 Avenida Venusto, San Diego, CA, U.S.A',
             'language': 'ca'}
# response = requests.get(base_url, params = my_params)
response = requests.get(base_url)
# results = response.json()['results']
# x_geo = results[0]['geometry']['location']
# print(x_geo['lng'], x_geo['lat'])

results = response.json()[0]["price_usd"]
print(results)
