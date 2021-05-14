from Stats import Stats
from RarityEnum import Rarity


class Item:

    # Attributes
    name: str
    stats: Stats
    rarity: Rarity

    # Methods
    def __init__(self, name: str, stats: Stats, rarity: Rarity):
        self.name = name
        self.stats = stats
        self.rarity = rarity


class Weapon(Item) :

    damage : float
    mag_ratio : float
    phys_ratio : float

    def __init__(self, name : str, stats : Stats, rarity : Rarity, damage : double, mag_ratio : double, phys_ratio : double):
        self.damage = damage
        self.mag_ratio = mag_ratio
        self.phys_ratio = phys_ratio

        super(Weapon, self).__init__(str, stats, rarity)


class Armor(Item) :

    armor : float
    mag_ratio : float
    phys_ratio : float

    def __init__(self, name : str, stats : Stats, rarity : Rarity, armor : float, mag_ratio : double, phys_ratio : double):

        self.armor = armor
        self.mag_ratio = mag_ratio
        self.phys_ratio = phys_ratio

        super(Armor, self).__init__(str, stats, rarity)

