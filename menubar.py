import logging
from collections import OrderedDict
from typing import Hashable, Dict
import rumps

from menu_callbacks.base import MenuItemInterface
from processors.base import DataProcessorInterface

TITLE_REFRESH_SEC = 1


class AlreadyExists(Exception):
    pass


class NoProcessors(Exception):
    pass


class App(rumps.App):
    def __init__(self):
        self.app = rumps.App("App", "Loading...")
        self.processors: Dict[DataProcessorInterface, rumps.Timer] = OrderedDict()

        self.render_title_timer = rumps.Timer(self.render_title, TITLE_REFRESH_SEC)

    def register_processor(self, processor: DataProcessorInterface) -> "App":
        if not processor.period_sec:
            raise ValueError('Run period should be specified in seconds')
        if processor in self.processors:
            raise AlreadyExists
        self.processors[processor] = rumps.Timer(processor.run, processor.period_sec)
        return self

    def register_menu_callback(self, menucallback: MenuItemInterface) -> "App":
        m_action = rumps.MenuItem(menucallback.get_name(), menucallback.run)
        self.app.menu.add(m_action)
        logging.info(f'Added new menu item {menucallback.get_name()}')
        return self

    def render_title(self, *args, **kwargs) -> None:
        title = ' | '.join([h.get_title() for h in self.processors])
        self.app.title = title

    def run(self) -> None:
        if not len(self.processors):
            raise NoProcessors('Add at least one processor')

        logging.info('Starting timers')
        for processor, timer in self.processors.items():
            timer.start()
            logging.debug('Started timer for processor %s', processor.name)
        self.render_title_timer.start()
        logging.info('Starting app')
        self.app.run()