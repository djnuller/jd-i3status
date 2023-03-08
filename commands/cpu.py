import psutil
from commands.decorators import Decorators
from commands.command import Command

decorators = Decorators()

class Cpu:
    def __init__(self):
        pass

    def cpu_load(self, color, bg_color):
        cpu_percent = psutil.cpu_percent(interval=1)
        msg = Command(
            name="id_cpu_usage",
            full_text=f"CPU load: {cpu_percent}%",
            background=color
        )
        decorators.print_command(msg.get(), color, bg_color)