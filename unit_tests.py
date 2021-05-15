import unittest
from Stats import Stats
from Entity import Entity
from Item import Weapon, Armor
from Generators import Generators
from RarityEnum import Rarity


class Test_Stats(unittest.TestCase):
    def setUp(self):
        self.stats = Stats([2, 2, 2, 2, 2])

    def test_Stats_constructor(self):
        self.assertRaises(ValueError, Stats, [2])

    def test_get_strength(self):
        self.assertEqual(self.stats.get_strength(), 2)

    def test_get_attack(self):
        self.assertEqual(self.stats.get_attack(), 2)

    def test_get_magic(self):
        self.assertEqual(self.stats.get_magic(), 2)

    def test_get_agility(self):
        self.assertEqual(self.stats.get_agility(), 2)

    def test_get_defense(self):
        self.assertEqual(self.stats.get_defense(), 2)


class Test_Entity(unittest.TestCase):
    def setUp(self):
        self.entity_stats = Generators.random_stats(10, 20)
        self.stuff_stats = Stats.create_with_value(10)

        self.stuff = list([
            Weapon("Sword", self.stuff_stats, Rarity.NORMAL, 10, 15, 0.8, 0.2),
            Armor("Chastplate", self.stuff_stats, Rarity.EPIC, 5, 6, 0.4, 0.6)
        ])

        self.entity = Entity("Entity", self.entity_stats, self.stuff)

    def test_constructor(self):
        pass

    def test_do_damage(self):
        pass

    def test_get_weapon_stats(self):
        pass

    def test_get_armor_stats(self):
        pass

    def test_compute_hit_damage(self):
        pass

    def test_take_damage(self):
        pass

    def test_compute_hp(self):
        pass

    def test_compute_total_stats(self):
        pass
