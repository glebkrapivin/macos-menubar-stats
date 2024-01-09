import logging
from typing import Protocol


class DataProcessorInterface(Protocol):
    n_retries: int
    period_sec: int

    def run(self, *args, **kwargs):
        pass

    def get_title(self, *args, **kwargs) -> str:
        pass


class BaseProcessor:

    def __init__(self, period_sec: int, n_retries: int = 1, *args, **kwargs):
        if n_retries <= 0:
            raise ValueError('Retries should be greater than 0')
        if period_sec <= 0:
            raise ValueError('Period should be greater than 0')
        self.n_retries = n_retries
        self.period_sec = period_sec

        self._title = ""
        self.name = self.__class__.__name__

    def get_data(self) -> str:
        return 'example'

    def get_title(self, *args, **kwargs) -> str:
        return self._title

    def run(self, *args, **kwargs):
        for r in range(1, self.n_retries + 1):
            logging.info('Started %s retry # %s', self.name, r)
            try:
                self._title = self.get_data()
                logging.info('got value %s from %s', self._title, self.name)
            except Exception as e:
                logging.exception('Error while processing %s', self.name)

            