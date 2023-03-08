import psutil
import math
from hurry.filesize import size
from commands.decorators import Decorators
from commands.command import Command

decorators = Decorators()

class Memory():
    def __init__(self) -> None:
        self.virtual_memory = psutil.virtual_memory()

    def get_memory_load(self, color, bg_color):
        memory = self.virtual_memory[2]
        msg = Command(
            name="id_memory",
            full_text=f"Mem load: {memory}%",
            background=color
        )
        decorators.print_command(msg.get(), color, bg_color)
    
    def get_total_amount(self, color, bg_color):
        memory = self.virtual_memory[0]
        msg = Command(
            name="memory_total",
            full_text=f"Mem total: {size(memory)}",
            background=color
        )
        decorators.print_command(msg.get(), color, bg_color)

    def get_available_amount(self, color, bg_color):
        memory = self.virtual_memory[1]
        msg = Command(
            name="memory_available",
            full_text=f"Mem total: {size(memory)}",
            background=color
        )
        decorators.print_command(msg.get(), color, bg_color)

    def get_pretty(self, color, bg_color):
        memory = self.virtual_memory
        mem_load = str(memory[2])
        text = f"Mem: L {mem_load}% - A/T {size(memory[1])}/{size(memory[0])}"
        msg = Command(
            name="memory_pretty",
            full_text=text,
            background=color
        )
        decorators.print_command(msg.get(), color, bg_color)