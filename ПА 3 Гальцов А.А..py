import requests

def get_currency_exchange():
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data = response.json()
    usd_rate = data['Valute']['USD']['Value']
    eur_rate = data['Valute']['EUR']['Value']
    difference = usd_rate / eur_rate
    return difference

print(get_currency_exchange())