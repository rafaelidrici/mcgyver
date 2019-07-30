from position import Position
from map import Map

def main():
    map = Map('data/map1.txt')

    # Debugging the map position
    p = Position(2, 2).down
    print(map.is_valid(p))

if  __name__ == "__main__":
    main()