from commands.decorators import Decorators
from commands.command import Command
from lib.ip import Ip

decorators = Decorators()
ip_utils = Ip()

class Network:
    def __init__(self):
        pass

    def public_ip(self, color, bg_color):
        res = ip_utils.get_public_ip_info()
        info = f"pub ip: {res.get('ip')} - {res.get('city')} - {res.get('country_code')}"
        msg = Command(
            name="public_ip",
            full_text=info,
            background=color
        )
        decorators.print_command(msg.get(), color, bg_color)

    def local_ip(self, color, bg_color):
        info = f"local ip: {ip_utils.get_local_ip()}"
        msg = Command(
            name="local_ip",
            full_text=info,
            background=color
        )
        decorators.print_command(msg.get(), color, bg_color)