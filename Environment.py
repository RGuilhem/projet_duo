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
        self.connected_map = [[0]*len(self.rooms) for lgn in range(len(self.rooms))]

        for room in rooms:
            self.map[room.position_x][room.position_y] = room.number

        # i (lines) goes from 0 to (len(self.rooms)-1) in the list of rooms
        for i in range(len(self.rooms)):
            # j (columns) goes from (i+1) to (len(self.rooms)-1) in the list of rooms
            for j in range(i + 1, len(self.rooms)):
                if Level.is_connected(self.rooms[i], self.rooms[j], len(self.rooms)):
                    self.connected_map[i][j] = 1  # input value to upper_triangle of connected_map's matrix
                    self.connected_map[j][i] = 1  # input value to lower_triangle of connected_map's matrix

    def show_map(self):
        for i in range(len(self.rooms)):
            for j in range(len(self.rooms)):
                print("{:<2}".format(self.map[i][j]), end=" ")
            print()


    def generate_connected_map(self):
        pass

    def is_connected(self, room : "Room", mini_map):
        if mini_map[room.position_x-1][room.position_y] != 0:
            return True
        if mini_map[room.position_x][room.position_y+1] != 0:
            return True
        if mini_map[room.position_x+1][room.position_y] != 0:
            return True
        if mini_map[room.position_x][room.position_y-1] != 0:
            return True
        return False


class Room:
    monsters: list[Monster]
    position_x: int
    position_y: int
    biome: "Biome"
    number: int

    # shape : ????????????

    def __init__(self, monsters: list[Monster], position_x: int, position_y: int, number: int, biome: "Biome"):
        self.monsters = monsters
        self.position_x = position_x
        self.position_y = position_y
        self.number = number
        self.biome = biome


class Biome:
    pass





if __name__ == "__main__":
    room1 = Room(None, 0, 0, None)
    room2 = Room(None, 0, 2, None)
    room3 = Room(None, 2, 0, None)
    room4 = Room(None, 1, 2, None)

    room_list = [room_1, room_2, room_3, room_4]

    level1 = Level(1, room_list, None, None)
    level1.show_map()
    print()
    level1.show_connected_map()
