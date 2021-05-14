from Stats import Stats
from Item import Item

class Entity:

    # Attributes
    name: str
    hp: int
    lvl: int
    base_stats: Stats
    total_stats: Stats
    stuff: list[Item]
    position = [0] * 2

    # Methods
    def __init__(self, name: str, base_stats: Stats, stuff: list[Item]):
        self.name = name
        self.base_stats = base_stats
        self.stuff = stuff
        self.hp = self.compute_hp(base_stats)
        self.lvl = 0

    def do_damage(self, target):
        pass

    def take_damage(self, damage):
        pass

    @staticmethod
    def compute_hp(player_stats: Stats):
        pass

    def compute_total_stats(self, base_stats: Stats):
        for item in self.stuff:
            self.base_stats += item.stats

    def __str__(self):
        return f"{self.name}: Level {self.lvl}"


if __name__ == "__main__":
    entity = Entity("Player", Stats([1, 2, 3, 4, 5]))
    print(entity)
