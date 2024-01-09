import logging

from miio import AirPurifierMiot

from processors.base import BaseProcessor


class BadQualityInside(BaseProcessor):
    def __init__(self, ip, token, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.p = AirPurifierMiot(ip=ip, token=token)

    def get_data(self) -> str:

        try:
            pm25 = self.p.status().aqi

            if pm25 < 20:
                return '🟢'

        except Exception as e:
            logging.exception(e)
            pass

        return '🔴'
