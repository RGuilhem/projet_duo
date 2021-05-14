from Item import Item
import random
from Stats import Stats
from RarityEnum import Rarity


class Generators:

    @staticmethod
    def random_item() -> Item:
        f = open("fantasy_names.txt")
        content = f.read()
        f.close()
        names = content.split("\n")
        item_name = f"{random.choice(names)}'s item"
        rarity = random.choice(list(Rarity))
        stats = Generators.random_stats(10, 25)
        return Item(item_name, stats, rarity)

    @staticmethod
    def random_unique():
        pass

    @staticmethod
    def random_stats(min_stats: int, max_stats: int) -> Stats:
        temp = Stats.create_empty()
        for key in list(temp.values):
            temp.values[key] = random.randrange(min_stats, max_stats)
        return temp


if __name__ == "__main__":
    for i in range(5):
        print(Generators.random_item())
