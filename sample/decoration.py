class Factory():
    def __init__(self, name) -> None:
        self.name = name
    
    @classmethod
    def whatsName(cls, name_str):
        name = name_str.split(':')[1]
        return cls(name)
    
    def print_name(self):
        print(self.name)

