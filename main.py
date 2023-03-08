from commands import cpu, network, decorators, misc, memory
import time



class Status:

    def __init__(self):
        self.cpu = cpu.Cpu()
        self.network = network.Network()
        self.decorators = decorators.Decorators()
        self.misc = misc.Misc()
        self.memory = memory.Memory()

    def _commands(self):
        self.misc.get_time("#264653", "#000000")
        print(',')
        self.memory.get_pretty("#2a9d8f", "#264653")
        print(',')
        self.cpu.cpu_load("#e9c46a", "#2a9d8f")
        print(',')
        self.network.local_ip("#f4a261", "#e9c46a")
        print(',')
        self.network.public_ip("#e76f51", "#f4a261")
    
    def run(self):
        self.decorators.print_init()
        while True:
            print(',[')
            self._commands()
            print(']')
            time.sleep(1)

if __name__ == "__main__":
    status = Status()
    status.run()
