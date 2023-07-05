import urllib.parse
import uuid

import pyperclip


class MeetzoneMenuItem:
    BASE_URL = "https://meetzone.o3.ru/"

    def run(self, *args, **kwargs):
        url = urllib.parse.urljoin(self.BASE_URL, str(uuid.uuid4()))
        pyperclip.copy(url)

    def get_name(self):
        return "🧑‍💻Meetzone"
