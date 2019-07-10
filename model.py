
class Position:

    def __init__(self, x, y):
        self.position = (x, y)
    
    def __repr__(self):
        return str(self.position)

    def up(self):
        x, y = self.position
        return Position(x-1, y)

    def down(self):
        x, y = self.position
        return Position(x+1, y)

    def right(self):
        x, y = self.position
        return Position(x, y+1)
    
    def left(self):
        x, y = self.position
        return Position(x, y-1)

class Player:
    # 
    def __init__(self, x, y):
        self.position = (1, 1)

class Guardian:
    pass
    
class Item:
    pass

class Zone:
    pass


    
