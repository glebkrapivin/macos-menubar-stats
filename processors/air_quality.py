import requests
from bs4 import BeautifulSoup

from processors.base import BaseProcessor



class AirQualityProcessor(BaseProcessor):
    def __init__(self, url: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url

    def get_data(self) -> str:

        r = requests.get('https://www.iqair.com/kazakhstan/almaty-qalasy/almaty/tulebaeva-82', timeout=5)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find_all('table', class_="aqi-overview-detail__other-pollution-table")[0]

        for item in list(list(table.children)[1].children):
            if "PM2.5" in list(item.children)[0].text:
                return str(int(float(list(item.children)[2].text.replace('µg/m³', ''))))
