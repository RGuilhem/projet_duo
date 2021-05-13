from enum import Enum

class Monster(Entity) :

    # Pre-existing attributes
    '''
        name : str
        hp : int
        lvl : int
        base_stats : Stats
        total_stats : Stats
        stuff : List[Item]
        position : int[2]
     '''

    # Attributes
    is_aggro : bool
    rank : enum[Rank]

    def __init__(self, monster_rank : Rank, monster_stats : Stats, stuff : List[Item]):

        self.rank = monster_rank

        if rank == 1 :
            name.append("minion")
        elif rank == 2 :
            name.append("elite")
        else :
            name.append("sovereign")

        self.base_stats = monster_stats
        self.stuff = stuff
        self.hp = Entity.compute_hp(monster_stats)
        self.lvl = 0
        self.position = [0] * 2
        self.is_aggro = False



class Rank(Enum) :
    MINION = 1
    ELITE = 2
    SOVEREIGN = 3
