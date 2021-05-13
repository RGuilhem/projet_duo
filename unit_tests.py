import unittest
from Stats import Stats


class Test_Stats_Object(unittest.TestCase):

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
