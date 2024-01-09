import requests
from bs4 import BeautifulSoup

from processors.base import BaseProcessor


def InvLinear(AQIhigh, AQIlow, Conchigh, Conclow, a):
    c=((a-AQIlow)/(AQIhigh-AQIlow))*(Conchigh-Conclow)+Conclow
    return c


def ConcPM25(a):
    if (a>=0 and a<=50):
        ConcCalc=InvLinear(50,0,12,0,a)
    elif (a>50 and a<=100):
        ConcCalc=InvLinear(100,51,35.4,12.1,a)
    elif  (a>100 and a<=150):
        ConcCalc=InvLinear(150,101,55.4,35.5,a)
    elif  (a>150 and a<=200):
        ConcCalc=InvLinear(200,151,150.4,55.5,a)
    elif (a>200 and a<=300):
        ConcCalc=InvLinear(300,201,250.4,150.5,a)
    elif (a>300 and a<=400):
        ConcCalc=InvLinear(400,301,350.4,250.5,a)
    elif (a>400 and a<=500):
        ConcCalc=InvLinear(500,401,500.4,350.5,a)

    return ConcCalc


def get_pm_new():
    r = requests.get('https://api2.waqi.info/api/feed/@A116437/now.json')
    r = r.json()
    aqi = float(r["rxs"]["obs"][0]["msg"]["aqi"])

    return ConcPM25(aqi)

class AirQualityProcessor(BaseProcessor):
    def __init__(self, url: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url

    def get_data(self) -> str:

        # r = requests.get('https://www.iqair.com/kazakhstan/almaty-qalasy/almaty/tulebaeva-82', timeout=5)
        # soup = BeautifulSoup(r.content, 'html.parser')
        # table = soup.find_all('p', class_="aqi-value__value")[0]
        r = requests.get('https://api2.waqi.info/api/feed/@A116437/now.json')
        r = r.json()
        aqi = float(r["rxs"]["obs"][0]["msg"]["aqi"])
        return str(aqi)

        # for item in list(list(table.children)[1].children):
        #     if "PM2.5" in list(item.children)[0].text:
                # return str(int(float(list(item.children)[2].text.replace('µg/m³', ''))))
