import requests

from processors.base import BaseProcessor

BINANCE_URL = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"


class USDTProcessor(BaseProcessor):

    def __init__(self, paytype: str = "TinkoffNew", fiat: str = "RUB", trade_type: str = "BUY", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.paytype = paytype
        self.fiat = fiat
        self.trade_type: str = trade_type

    def get_data(self):
        request_data = {
            "proMerchantAds": False,
            "page": 1,
            "Rows": 1,
            "PayTypes": [self.paytype],
            "Asset": "USDT",
            "Fiat": self.fiat,
            "TradeType": self.trade_type
        }
        r = requests.post(BINANCE_URL, json=request_data)
        r.raise_for_status()
        response = r.json()
        return str(response["data"][0]["adv"]["price"])
