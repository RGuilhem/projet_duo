from Stats import Stats
from Item import Item, Weapon, Armor
from random import random


class Entity:
    """
    Base class for living entities in the game
    """
    # Attributes
    name: str
    hp: int
    lvl: int
    base_stats: Stats
    total_stats: Stats
    stuff: list[Item]
    position = [0] * 2

    def __init__(self, name: str, base_stats: Stats, stuff: list[Item]):
        """
        Entity constructor:
        -name: str = the name of the entity constructed
        -base_stats: Stats = the caracteristics of the entity in the form of
        a Stats object
        """
        self.name = name
        self.base_stats = base_stats
        self.stuff = stuff
        self.compute_total_stats()
        self.hp = 100
        self.lvl = 0
        self.compute_hp()

    def do_damage(self, target: "Entity") -> None:
        """
        Function called when an entity attacks another
        -target: Entity = the target that is attaccked
        """
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

    def get_weapon_stats(self) -> list(float):
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

    def compute_hit_damage(self) -> int:
        """
        Calculate the damage of an attack depending on the weapon
        items and stats on an entity
        return: int = the total damage that should be inflicted by the
        hit
        """
        damage = 0
        #TODO implement calculation
        return damage

    def take_damage(self, damage: int) -> None:
        """
        Apply the damage of an attack to it's target after accounting
        for damage mmmitigation, this function is called by the do_damage
        function of the attacker
        -damage: int = the raw damage of the attacck received
        """
        pass

    def compute_damage_mitigation(self) -> float:
        """
        Calculate the damage mitigation of the entity depending on it's
        armor stat
        return: float = number between 0 and 1, 0 mean 100% mitigation
        """
        pass

    def compute_hp(self) -> None:
        """
        Calculate the total hp based on the stats with formula:
        hp = 100 + 10*lvl each strength point add 1% hp
        """
        self.hp = int((100 + 10 * self.lvl) *
                      (1 + self.total_stats.get_strength() * 0.01))

    def compute_total_stats(self) -> None:
        """
        Compute the total stats of an entity, meaning it's based stats
        added to the stats of it's items
        """
        self.total_stats = Stats.create_empty()
        self.total_stats += self.base_stats
        for item in self.stuff:
            self.total_stats += item.stats

    def __str__(self) -> int:
        return f"{self.name}: Level {self.lvl}\n{self.total_stats}"


if __name__ == "__main__":
    pass
