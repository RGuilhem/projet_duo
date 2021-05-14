from Item import Item
import random
from Stats import Stats
from RarityEnum import Rarity


class Generators:

    @staticmethod
    def random_item():
        f = open("fantasy_names.txt")
        content = f.read()
        names = content.split("\n")
        item_name = f"{random.choice(names)}'s item"
        rarity = random.choice(Rarity)

    @staticmethod
    def random_unique():
        pass

    @staticmethod
    def random_stats(max_stats: int):
        temp = Stats.create_empty()
        for key in list(temp.values):
            temp.values[key] = random.randrange(0, max_stats)
        return temp


if __name__ == "__main__":
    st1 = Generators.random_stats(10)
    print(st1)
