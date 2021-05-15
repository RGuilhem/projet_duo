from Stats import Stats
from Item import Item, Weapon, Armor
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
        self.compute_hp()

    def do_damage(self, target) -> None:
        att = self.total_stats.get_attack()
        enn_agi = target.total_stats.get_agility()
        if att <= enn_agi:
            hit_chance = (0.5 * att / enn_agi)
        else:
            hit_chance = (1 - 0.5 * enn_agi / att)
        print(hit_chance)
        if random() < hit_chance:
            print("hit")
        else:
            print("miss")

    def get_weapon_stats(self):
        """
        Return a list containing the specials stats of the Enity's weapon
        return : list([damage, mag_ratio, phys_ratio])
        """
        for item in self.stuff:
            if isinstance(item, Weapon):
                return list([item.damage, item.mag_ratio, item.phys_ratio])

    def get_armor_stats(self):
        """
        Return a list containing the specials stats of the Enity's armor
        return : list([armor, mag_ratio, phys_ratio])
        """
        for item in self.stuff:
            if isinstance(item, Armor):
                return list([item.armor, item.mag_ratio, item.phys_ratio])

    def compute_hit_damage(self, target) -> int:
        damage = 0
        #TODO implement calculation
        return damage

    def take_damage(self, damage) -> None:
        pass

    def compute_hp(self) -> None:
        self.hp = int((100 + 10 * self.lvl) *
                      (1 + self.total_stats.get_strength() * 0.01))

    def compute_total_stats(self) -> None:
        self.total_stats = Stats.create_empty()
        self.total_stats += self.base_stats
        for item in self.stuff:
            self.total_stats += item.stats

    def __str__(self) -> int:
        return f"{self.name}: Level {self.lvl}\n{self.total_stats}"


if __name__ == "__main__":
    pass
