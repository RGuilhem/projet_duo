from Stats import Stats
from Item import Item
from random import random


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
        self.compute_total_stats()
        self.hp = 100
        self.lvl = 0 

    def do_damage(self, target) -> None:
        att = self.total_stats.get_attack()
        enn_agi = target.total_stats.get_agility()
        if att <= enn_agi:
            hit_chance = (0.5*att/enn_agi)
        else:
            hit_chance = (1-0.5*enn_agi/att)
        print(hit_chance)
        if random() < hit_chance:
            print("hit")
        else:
            print("miss")

    def take_damage(self, damage) -> None:
        pass

    def compute_hp(self, layer_stats: Stats) -> None:
        self.hp = int((100 + 10*self.lvl) * self.total_stats.get_strength()*0.01)

    def compute_total_stats(self) -> None:
        self.total_stats = Stats.create_empty()
        self.total_stats += self.base_stats
        for item in self.stuff:
            self.total_stats += item.stats

    def __str__(self) -> int:
        return f"{self.name}: Level {self.lvl}"


if __name__ == "__main__":
    entity = Entity("Player", Stats([0, 24, 0, 0, 0]), [Item("i1", Stats([0, 2, 0, 0, 0]), None)])
    target = Entity("Target", Stats([0, 0, 0, 6, 0]), [Item("i2", Stats([0, 0, 0, 2, 0]), None)])
    print(entity.hp)

