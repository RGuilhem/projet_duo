from Entity import *

class Player(Entity) :

    #Pre-existing attributes
    """
        name : str
        hp : int
        lvl : int
        base_stats : Stats
        total_stats : Stats
        stuff : List[Item]
        position : int[2]
     """

    # Attributes

    inventory : List[Item]

    # Methods
    def __init__(self, player_name : str, player_stats : Stats, stuff : List[Item]):
        self.name = player_name
        self.base_stats = player_stats
        self.stuff = stuff
        self.hp = Entity.compute_hp(player_stats)
        self.lvl = 0
        self.position = [0] * 2



    @staticmethod
    def move(self, x : int, y : int) -> int[2]:
        self.position[0] += x
        self.position[1] += y
        return position

def main():
    print("Hello world")

if __name__ == "__main__" :
    main()