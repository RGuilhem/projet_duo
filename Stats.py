class Stats:

    values: dict = dict([("strength", 0), ("attack", 0), ("magic", 0),
                         ("agility", 0), ("defense", 0)])

    def __init__(self, stat_list) -> "Stats":
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
    def create_empty() -> "Stats":
        return Stats([0, 0, 0, 0, 0])

    @staticmethod
    def create_with_value(value: int) -> "Stats":
        return Stats([value]*5)

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

    def copy(self) -> "Stats":
        temp = Stats.create_empty()
        for key in list(self.values):
            temp.values[key] = self.values[key]
        return temp

    def __add__(self, other: "Stats") -> "Stats":
        if not isinstance(other, Stats):
            raise ValueError(
                "It's only possible to   add two Stats objects together")

        temp = Stats.create_empty()
        for key in list(self.values):
            temp.values[key] = self.values[key] + other.values[key]
        return temp

    def __iadd__(self, other: "Stats") -> "Stats":
        return self + other

    def __mul__(self, other: float) -> "Stats":
        temp = self.copy()
        for key in list(self.values):
            temp.values[key] = int(self.values[key] * other)
        return temp

    def __imul__(self, other: float) -> "Stats":
        return self * other

    def __str__(self) -> str:
        string = ""
        for key in list(self.values):
            string += f"{key}: {self.values[key]}\n"
        return string


if __name__ == "__main__":
    s1 = Stats([10, 2, 3, 4, 5])
    s2 = Stats([5, 4, 3, 2, 1])
    print(s1*1.2)
