class Command:
    def __init__(self, name: str, full_text: str, background: str, color = "#ffffff"):
        self.name = name
        self.full_text = full_text
        self.background = background
        self.color = color
    
    def get(self):
        return {
            'name': self.name,
            'full_text': f"{self.full_text}  ",
            'background': self.background,
            'color': self.color
        }
        