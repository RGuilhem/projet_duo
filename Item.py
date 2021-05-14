from Stats import Stats
from RarityEnum import Rarity


class Item:

    # Attributes
    name: str
    stats: Stats
    rarity: Rarity
    RARITY_MULTIPLIERS: list[float] = [1, 1.2, 1.4, 1.6, 1.8]

    # Methods
    def __init__(self, name: str, stats: Stats, rarity: Rarity):
        self.name = name
        self.stats = stats * Item.RARITY_MULTIPLIERS[rarity.value]
        self.rarity = rarity

    def __str__(self):
        return f"{str(self.name)} {self.rarity}\n STATS :\n{self.stats}"


class Weapon(Item):

    damage: float
    mag_ratio: float
    phys_ratio: float

    def __init__(self, name: str, stats: Stats, rarity: Rarity, damage: float,
                 mag_ratio: float, phys_ratio: float):
        mult = Item.RARITY_MULTIPLIERS[rarity.value]
        self.damage = int(damage * mult)
        self.mag_ratio = round(mag_ratio * mult, 2)
        self.phys_ratio = round(phys_ratio * mult, 2)

        super(Weapon, self).__init__(name, stats, rarity)

    def __str__(self) -> str():
        return f"{super().__str__()}Damage: {self.damage}\nMagicRatio: {self.mag_ratio}\nPhysical Ratio: {self.phys_ratio}\n"


class Armor(Item):

    armor: float
    mag_ratio: float
    phys_ratio: float

    def __init__(self, name: str, stats: Stats, rarity: Rarity, armor: float,
                 mag_ratio: float, phys_ratio: float):
        mult = Item.RARITY_MULTIPLIERS[rarity.value]
        self.armor = int(armor * mult)
        self.mag_ratio = round(mag_ratio * mult, 2)
        self.phys_ratio = round(phys_ratio * mult, 2)

        super(Armor, self).__init__(name, stats, rarity)


    def __str__(self) -> str():
        return f"{super().__str__()}Armor: {self.armor}\nMagicRatio: {self.mag_ratio}\nPhysical Ratio: {self.phys_ratio}\n"


if __name__ == "__main__":
    s = Stats([10, 15, 12, 15, 11])
    print(Item("test_item", s, Rarity.NORMAL))
    for r in Rarity:
        item = Armor("item", s, r, 10, 0.8, 0.2)
        print(item)
