from typing import Protocol


class MenuItemInterface(Protocol):

    def run(self, *args, **kwargs) -> None:
        pass

    def get_name(self, *args, **kwargs) -> str:
        pass