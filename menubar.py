import logging
from collections import OrderedDict

import rumps

from processors.base import BaseProcessor

TITLE_REFRESH_SEC = 1


class AlreadyExists(Exception):
    pass


class NoProcessors(Exception):
    pass


class App:
    def __init__(self):
        self.app = rumps.App("App", "Loading...")
        self.processors = OrderedDict()

        self.render_title_timer = rumps.Timer(self.render_title, TITLE_REFRESH_SEC)

    def register_handler(self, processor: BaseProcessor) -> "App":
        if not processor.period_sec:
            raise ValueError('Run period should be specified in seconds')
        if processor in self.processors:
            raise AlreadyExists
        self.processors[processor] = rumps.Timer(processor.run, processor.period_sec)
        return self

    def render_title(self, *args, **kwargs):
        title = ' '.join([h.title for h in self.processors])
        self.app.title = title

    def run(self):
        if not len(self.processors):
            raise NoProcessors('Add at least one processor')

        logging.info('Starting timers')
        for processor, timer in self.processors.items():
            timer.start()
            logging.debug('Started timer for processor %s', processor.name)
        self.render_title_timer.start()
        logging.info('Starting app')
        self.app.run()
