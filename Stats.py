class Stats:

    values: dict = dict([("strength", 0), ("attack", 0), ("magic", 0),
                         ("agility", 0), ("defense", 0)])

    def __init__(self, stat_list):
        if len(self.values) != len(stat_list):
            raise ValueError(
                "the length of the stat_list argument must be equal to the number of stats"
            )
        keys = list(self.values)
        for i in range(len(stat_list)):
            self.values[keys[i]] = stat_list[i]

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
