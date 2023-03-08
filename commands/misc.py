from datetime import datetime
from commands.decorators import Decorators
from commands.command import Command

decorators = Decorators()

class Misc:
    def __init__(self):
        pass

    def get_time(self, color, bg_color):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S - %d-%m-%y")
        msg = Command(
            name="time",
            full_text=current_time,
            background=color
        )
        decorators.print_command(msg.get(), color, bg_color)

