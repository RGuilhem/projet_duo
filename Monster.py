from enum import Enum
from Entity import Entity
from Stats import Stats
from Item import Item
from RarityEnum import Rarity

class Monster(Entity):

    # Pre-existing attributes
    '''
        name : str
        hp : int
        lvl : int
        base_stats : Stats
        total_stats : Stats
        stuff : List[Item]
        position : int[2]
     '''

    # Attributes
    is_aggro: bool
    rank: "Rank"

    def __init__(self, name: str, base_stats: Stats,
                 stuff, rank: "Rank") -> None:

        super().__init__(name, base_stats, stuff)
        self.rank = rank
        self.is_aggro = False

    def __str__(self) -> str:
        return f"{str(self.rank)} {super().__str__()}"


class Rank(Enum):
    MINION = 1
    ELITE = 2
    SOVEREIGN = 3

    def __str__(self) -> str:
        return f"{self.name} "


if __name__ == "__main__":
    print(Monster("Blob", Stats([1, 2, 3, 4, 5]), [Item("item", Stats.create_empty(), Rarity.MAGICAL)], Rank.ELITE))
