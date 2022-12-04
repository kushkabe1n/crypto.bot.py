import requests
import json
from config import keys

class ConvertionException(Exception):
    pass


class CryptoConvecter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_tiker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}. ')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}. ')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}. ')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tiker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base
