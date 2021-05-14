from enum import Enum


class Rarity(Enum):
    NORMAL = 0
    MAGICAL = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4

    def __str__(self):
        return f"{self.name}"
 
