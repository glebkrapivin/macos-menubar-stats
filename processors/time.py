from datetime import datetime

import pytz

from processors.base import BaseProcessor


class CurrentTimeProcessor(BaseProcessor):

    def __init__(self, timezone_str: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timezone = pytz.timezone(timezone_str)

    def get_data(self) -> str:
        return str(datetime.now(self.timezone).time())[:5]
