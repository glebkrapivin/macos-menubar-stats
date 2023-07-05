import logging

from menu_callbacks import MeetzoneMenuItem
from menubar import App
from processors import AirQualityProcessor

if __name__ == '__main__':
    logging.basicConfig(level='INFO')

    aq = AirQualityProcessor(url='https://www.iqair.com/kazakhstan/almaty-qalasy/almaty/tulebaeva-82',
                             n_retries=1,
                             period_sec=45)
    mz = MeetzoneMenuItem()

    a = App()
    a.register_processor(aq)
    a.register_menu_callback(mz)
    a.run()
