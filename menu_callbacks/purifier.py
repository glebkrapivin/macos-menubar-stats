import rumps
from miio import AirPurifierMiot


class PurifierMenuItem:

    def __init__(self, level, token, ip):
        self.p = AirPurifierMiot(ip=ip, token=token)
        self.level = level

    def run(self, *args, **kwargs):
        self.p.set_favorite_level(self.level)
        rumps.notification('Level set', subtitle=' ', message=f'Level was set to {self.level}')

    def get_name(self):
        return f"Xiaomi: Level {self.level}"


