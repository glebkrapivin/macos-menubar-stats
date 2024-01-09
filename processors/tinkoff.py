import requests

from processors.base import BaseProcessor

URL = "https://www.tinkoff.ru/api/trading/currency/get"

class TickerProcessor(BaseProcessor):

    def __init__(self, ticker: str = "USDRUB", reversed : bool= False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ticker = ticker
        self.reversed = reversed

    def get_data(self):
        d = {
            "ticker": self.ticker
        }
        r = requests.post(URL, json=d, timeout=3)
        r.raise_for_status()
        response = r.json()
        val = float(response["payload"]["prices"]["last"]["value"])
        if self.reversed:
            val = 1/val
        return '{:.2f}'.format(val)

