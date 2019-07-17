import settings as constants
from position import Position

class Map:

    def __init__(self, filename):
        self.filename = filename

        self._paths = set()
        self._start = set()
        self._goal = set()
        self._items = set()

        self.load_from_file()
    
    def is_valid(self, position):
        return position in self._paths

    def load_from_file(self):

        with open(self.filename) as infile:
            for x, line in enumerate(infile): #on lit chaque ligne
                for y, col in enumerate(line):
                    if col == constants.PATH:
                        self._paths.add(Position(x, y))
                    elif col == constants.STARTING_SPAWN:
                        self._start.add(Position(x, y))
                    elif col == constants.GUARDIAN_SPAWN:
                        self._goal.add(Position(x, y))

def main():
    map = Map('data/map1.txt')

    p = Position(2, 2).down
    print(map.is_valid(p))

if  __name__ == "__main__":
    main()
