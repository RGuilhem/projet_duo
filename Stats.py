class Stats:

    values: dict = dict([("strength", 0), ("attack", 0), ("magic", 0),
                         ("agility", 0), ("defense", 0)])

    def __init__(self, stat_list):
        if len(self.values) != len(stat_list):
            raise ValueError(
                "the length of the stat_list argument must be equal to the number of stats"
            )

        self.values = dict([("strength", 0), ("attack", 0), ("magic", 0),
                            ("agility", 0), ("defense", 0)])
        keys = list(self.values)
        for i in range(len(stat_list)):
            self.values[keys[i]] = stat_list[i]

    @staticmethod
    def create_empty():
        return Stats([0, 0, 0, 0, 0])

    def get_strength(self) -> int:
        return self.values["strength"]

    def get_attack(self) -> int:
        return self.values["attack"]

    def get_magic(self) -> int:
        return self.values["magic"]

    def get_agility(self) -> int:
        return self.values["agility"]

    def get_defense(self) -> int:
        return self.values["defense"]

    def __add__(self, other):
        if not isinstance(other, Stats):
            raise ValueError(
                "It's only possible to   add two Stats objects together")

        temp = Stats.create_empty()
        for key in list(self.values):
            temp.values[key] = self.values[key] + other.values[key]
        return temp

    def __str__(self):
        string = ""
        for key in list(self.values):
            string += f"{key}: {self.values[key]}\n"
        return string


if __name__ == "__main__":
    s1 = Stats([1, 2, 3, 4, 5])
    s2 = Stats([5, 4, 3, 2, 1])
    print(s1 + s2)
