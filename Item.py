from Stats import *
from RarityEnum import *

class Item :

    # Attributes
    name : str
    stats : Stats
    rarity : Rarity

    # Methods
    def __init__(self, name : str, stats : Stats, rarity : "Rarity"):
        self.name = name
        self.stats = stats
        self.rarity = rarity


