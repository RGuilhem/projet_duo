from Monster import *
from Player import *


class Dungeon:
    current_zone: "Zone"
    player: Player

    def __init__(self, current_zone: "Zone", player: Player):
        self.current_zone = current_zone
        self.player = player

    def next_zone(self):
        pass


class Zone:
    current_level: "Level"
    biome: "Biome"

    def __init__(self, current_level: "Level", biome: "Biome"):
        self.current_level = current_level
        self.biome = biome

    def next_level(self):
        pass


class Level:
    level: int
    biome: "Biome"
    rooms: list["Room"]
    level_monsters: list[Monster]

    def __init__(self, level: int, rooms: list["Room"], level_monsters: list[Monster], biome: "Biome"):
        self.level = level
        self.rooms = rooms
        self.biome = biome
        self.level_monsters = level_monsters
        self.map = [[0]*len(self.rooms) for lgn in range(len(self.rooms))]

        i = 1
        for room in rooms:
            self.map[room.position[0]][room.position[1]] = i
            i += 1

    def add_room(self, new_room: "Room"):
        pass

    def show_map(self):
        for i in range(len(self.rooms)):
            for j in range(len(self.rooms)):
                print("{:<2}".format(self.map[i][j]), end=" ")
            print()


class Room:
    monsters: list[Monster]
    position = [0] * 2
    biome: "Biome"

    # shape : ????????????

    def __init__(self, monsters: list[Monster], position_x: int, position_y: int, biome: "Biome"):
        self.monsters = monsters
        self.position = list([0, 0])
        self.position[0] = position_x
        self.position[1] = position_y
        self.biome = biome


class Biome:
    pass


if __name__ == "__main__":
    room1 = Room(None, 0, 0, None)
    room2 = Room(None, 0, 2, None)
    room3 = Room(None, 2, 0, None)
    room4 = Room(None, 1, 2, None)

    room_list = [room1, room2, room3, room4]

    level1 = Level(1, room_list, None, None)
    level1.show_map()
