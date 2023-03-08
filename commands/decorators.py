import json

class Decorators:
    def __init__(self):
        self.bg_bar_color = "#000000"

    def _seperator(self, color, bg_color):
        data = {}
        data['full_text'] = ""
        data['separator'] = False
        data['separator_block_width'] = 0
        data['border'] = self.bg_bar_color
        data['border_left'] = 0
        data['border_right'] = 0
        data['border_top'] = 2
        data['border_bottom'] = 2
        data['color'] = color
        data['background'] = bg_color
        return data

    def _common(self):
        data = {}
        data['border'] = self.bg_bar_color
        data['separator'] = False
        data['separator_block_width'] = 0
        data['border_left'] = 0
        data['border_right'] = 0
        data['border_top'] = 2
        data['border_bottom'] = 2
        return data
    
    def print_command(self, command, color, bg_color):
        command.update(self._common())
        print(f"{json.dumps(self._seperator(color, bg_color))}, {json.dumps(command)}")
    
    def print_init(self):
        print('{ "version": 1 }')
        print('[')
        print('[]')
    
    def print_end(self):
        print(']')
    
if __name__ == "__main__":
    test = Decorators()
    obj = {}
    obj['name'] = "test"
    obj['full_text'] = "Testersen"
    obj['background'] = "#1976D2"
    test.print_command(obj, "#1976D2")