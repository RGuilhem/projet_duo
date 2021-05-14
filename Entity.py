from Stats import Stats


class Entity:

    # Attributes
    name: str
    hp: int
    lvl: int
    base_stats: Stats
    total_stats: Stats
    #stuff: List[Item]
    position = [0] * 2

    # Methods
    def __init__(self, name: str, base_stats: Stats):
        self.name = name
        self.base_stats = base_stats
        #self.stuff = stuff
        self.hp = self.compute_hp(base_stats)
        self.lvl = 0

    def do_damage(self, target):
        pass

    def take_damage(self, damage):
        pass

    @staticmethod
    def compute_hp(player_stats: Stats):
        pass

    def compute_total_stats(self, base_stats: Stats):
        pass
