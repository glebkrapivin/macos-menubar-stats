import pyotp
import pyperclip


class TOTPMenuItem:

    def __init__(self, secret: str):
        self.totp = pyotp.TOTP(secret)

    def run(self, *args, **kwargs):
        return pyperclip.copy(self.totp.now())

    def get_name(self):
        return '🔐OTP'
