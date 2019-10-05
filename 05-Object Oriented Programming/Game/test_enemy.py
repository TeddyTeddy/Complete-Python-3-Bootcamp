import unittest
from enemy import Enemy, Troll, Vampyre


class TestVampyre(unittest.TestCase):
    def test_vampyre_default_init(self):
        vampyre = Vampyre('Drakula')
        self.assertEqual(vampyre.hit_points, 12)
        self.assertEqual(vampyre.lives, 3)

    def test_vampyre_take_damage_1(self):
        vampyre = Vampyre('Drakula')
        vampyre.take_damage(36)
        self.assertEqual(vampyre.hit_points, 0)
        self.assertEqual(vampyre.lives, 0)

    def test_vampyre_take_damage_2(self):
        vampyre = Vampyre('Drakula')  # hit_points=12, lives=3
        vampyre.take_damage(24)
        self.assertEqual(vampyre.hit_points, 12)
        self.assertEqual(vampyre.lives, 1)

    def test_vampyre_take_damage_3(self):
        vampyre = Vampyre('Drakula')  # hit_points=12, lives=3
        vampyre.take_damage(25)
        self.assertEqual(vampyre.hit_points, 11)
        self.assertEqual(vampyre.lives, 1)
        vampyre.take_damage(17)
        self.assertEqual(vampyre.hit_points, 0)
        self.assertEqual(vampyre.lives, 0)


class TestTroll(unittest.TestCase):
    def test_troll_default_init(self):
        troll = Troll(name='Ug')
        self.assertEqual(troll.name, 'Ug')
        self.assertEqual(troll.hit_points, 23)
        self.assertEqual(troll.lives, 1)

    def test_troll_take_damage_1(self):
        troll = Troll(name='Org')
        troll.take_damage(10)
        self.assertEqual(troll.hit_points, 13)
        self.assertEqual(troll.lives, 1)

        troll.take_damage(13)
        self.assertEqual(troll.hit_points, 0)
        self.assertEqual(troll.lives, 0)

        troll.take_damage(5)
        self.assertEqual(troll.hit_points, 0)
        self.assertEqual(troll.lives, 0)

    def test_troll_take_damage_2(self):
        troll = Troll(name='Org')
        troll.take_damage(100)
        self.assertEqual(troll.hit_points, 0)
        self.assertEqual(troll.lives, 0)

    def test_troll_take_damage_3(self):
        troll = Troll(name='Org')
        troll.take_damage(23)
        self.assertEqual(troll.hit_points, 0)
        self.assertEqual(troll.lives, 0)


class TestEnemy(unittest.TestCase):
    def test_negative_lives_at_enemy_init(self):
        with self.assertRaises(AssertionError):
            enemy = Enemy(name='Already Dead Enemy', hit_points=12, lives=-7)
        with self.assertRaises(AssertionError):
            enemy = Enemy(name='Already Dead Enemy', hit_points=12, lives=-1)

    def test_negative_hit_points_at_enemy_init(self):
        with self.assertRaises(AssertionError):
            enemy = Enemy(hit_points=-7, lives=1)
        with self.assertRaises(AssertionError):
            enemy = Enemy(hit_points=-1, lives=1)

    def test_default_values_in_enemy_init(self):
        enemy = Enemy()  # test with default init values: name="Enemy", hit_points=0, lives=1
        self.assertEqual(enemy.lives, 1)
        self.assertEqual(enemy.name, 'Enemy')
        self.assertEqual(enemy.hit_points, 0)

    def test_enemy_take_damage_1(self):
        enemy = Enemy(hit_points=30, lives=3)
        enemy.take_damage(damage=24)
        self.assertEqual(enemy.lives, 3)
        self.assertEqual(enemy.hit_points, 6)

        enemy.take_damage(damage=6)
        self.assertEqual(enemy.lives, 2)
        self.assertEqual(enemy.hit_points, 30)

        enemy.take_damage(damage=30)
        self.assertEqual(enemy.lives, 1)
        self.assertEqual(enemy.hit_points, 30)

        enemy.take_damage(damage=5)
        self.assertEqual(enemy.lives, 1)
        self.assertEqual(enemy.hit_points, 25)

        enemy.take_damage(damage=7)
        self.assertEqual(enemy.lives, 1)
        self.assertEqual(enemy.hit_points, 18)

        enemy.take_damage(damage=18)
        self.assertEqual(enemy.lives, 0)
        self.assertEqual(enemy.hit_points, 0)

        enemy.take_damage(damage=1)
        self.assertEqual(enemy.lives, 0)
        self.assertEqual(enemy.hit_points, 0)

    def test_enemy_take_damage_2(self):
        enemy = Enemy(hit_points=12, lives=1)
        enemy.take_damage(50)
        self.assertEqual(enemy.lives, 0)
        self.assertEqual(enemy.hit_points, 0)

        enemy.take_damage(30)
        self.assertEqual(enemy.lives, 0)
        self.assertEqual(enemy.hit_points, 0)

    def test_enemy_take_damage_3(self):
        enemy = Enemy(hit_points=500, lives=10)
        enemy.take_damage(5000)
        self.assertEqual(enemy.lives, 0)
        self.assertEqual(enemy.hit_points, 0)

    def test_enemy_take_damage_4(self):
        enemy = Enemy(hit_points=500, lives=10)
        enemy.take_damage(8000)
        self.assertEqual(enemy.lives, 0)
        self.assertEqual(enemy.hit_points, 0)

    def test_enemy_take_damage_5(self):
        enemy = Enemy(hit_points=12, lives=5)
        enemy.take_damage(24)
        self.assertEqual(enemy.lives, 3)
        self.assertEqual(enemy.hit_points, 12)

        enemy.take_damage(24)
        self.assertEqual(enemy.lives, 1)
        self.assertEqual(enemy.hit_points, 12)

        enemy.take_damage(12)
        self.assertEqual(enemy.lives, 0)
        self.assertEqual(enemy.hit_points, 0)


if __name__ == '__main__':
    unittest.main()
