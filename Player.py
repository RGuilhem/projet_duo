from Entity import Entity
from Stats import Stats
from Item import Item


class Player(Entity):

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

    #inventory : List[Item]

    # Methods
    def __init__(self, player_name: str, base_stats: Stats):
        super().__init__(player_name, base_stats)
        self.position = [0, 0]

    @staticmethod
    def move(self, x: int, y: int):
        self.position[0] += x
        self.position[1] += y


def main():

    obj = Player("Sylver", Stats([1, 2, 3, 4, 5]))
    print(obj.lvl, obj.position, obj.name)


if __name__ == "__main__":
    main()
