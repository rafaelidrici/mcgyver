from random import *

class Position:

    def __init__(self, x, y):
        self.position = (x, y)
    
    def __repr__(self):
        return str(self.position)

    def up(self):
        return Position(x-1, y)

    def down(self):
        return Position(x+1, y)

    def right(self):
        return Position(x, y+1)
    
    def left(self):
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


    
