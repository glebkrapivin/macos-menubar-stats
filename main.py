import logging

from menubar import App
from processors import CurrentTimeProcessor, AirQualityProcessor, USDTProcessor

if __name__ == '__main__':
    logging.basicConfig(level='INFO')

    aq = AirQualityProcessor(url='https://www.iqair.com/kazakhstan/almaty-qalasy/almaty/tulebaeva-82',
                             n_retries=1,
                             period_sec=45)
    ct = CurrentTimeProcessor(timezone_str="Europe/Moscow", period_sec=5)
    usdt = USDTProcessor(period_sec=60)

    a = App()
    a.register_handler(usdt)
    a.register_handler(aq)
    a.register_handler(ct)
    a.run()
