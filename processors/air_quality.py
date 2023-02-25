import requests
from bs4 import BeautifulSoup

from processors.base import BaseProcessor


class AirQualityProcessor(BaseProcessor):
    def __init__(self, url: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url

    def get_data(self) -> str:
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, 'html.parser')
        t = soup.find_all("p", class_="aqi-value__value")[0].text
        return t
