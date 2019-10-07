import unittest
from enemy import Enemy, Troll, Vampyre, VampyreKing

class TestVampyreKing(unittest.TestCase):
    def test_vampyre_king_default_init(self):
        vampyre_king = VampyreKing('Vampire King')
        self.assertEqual(vampyre_king.hit_points, 140)
        self.assertEqual(vampyre_king.lives, 3)

    def test_vampyre_king_take_damage(self):
        from random import randint
        vampyre_king = VampyreKing('Vampire King')
        while vampyre_king.lives != 0:
            damage = randint(1, 140)
            lives_b4 = vampyre_king.lives
            hit_points_b4 = vampyre_king.hit_points
            vampyre_king.take_damage(damage)
            self.assertTrue(TestVampyreKing._damage_inflicted_correctly(damage, lives_b4, hit_points_b4, vampyre_king))

    @staticmethod
    def _damage_inflicted_correctly(damage, lives_b4, hit_points_b4, vampyre_king):
        hit_points_per_life = 140
        damage_inflicted = damage // 4
        total_hit_points_b4 = (lives_b4 - 1) * hit_points_per_life + hit_points_b4
        remaining_hit_points = total_hit_points_b4 - damage_inflicted
        if remaining_hit_points <= 0:
            return vampyre_king.lives == 0 and vampyre_king.hit_points == 0
        else:
            if remaining_hit_points % hit_points_per_life == 0:
                return vampyre_king.lives == (remaining_hit_points // hit_points_per_life) and \
                       vampyre_king.hit_points == hit_points_per_life
            else:
                return vampyre_king.lives == ((remaining_hit_points // hit_points_per_life) + 1) and \
                       vampyre_king.hit_points == (remaining_hit_points % hit_points_per_life)

class TestVampyre(unittest.TestCase):
    """
    Important: Vampyre.take_damage function overrides Enemy.take_damage function.
    The overriding implementation adds random dogging(bypassing) ability to not
    to take the damage! This means that the test cases testing take_damage method
    will randomly fail at random places. This is expected and no need to attempt
    to fix the test cases
    """
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

    def test_vampyre_take_damage_4(self):
        vampyre = Vampyre('Drakula')  # hit_points=12, lives=3
        vampyre.take_damage(damage=12)
        self.assertEqual(vampyre.lives, 2)
        self.assertEqual(vampyre.hit_points, 12)

        vampyre.take_damage(damage=6)
        self.assertEqual(vampyre.lives, 2)
        self.assertEqual(vampyre.hit_points, 6)

        vampyre.take_damage(damage=3)
        self.assertEqual(vampyre.lives, 2)
        self.assertEqual(vampyre.hit_points, 3)

        vampyre.take_damage(damage=5)
        self.assertEqual(vampyre.lives, 1)
        self.assertEqual(vampyre.hit_points, 10)

        vampyre.take_damage(damage=7)
        self.assertEqual(vampyre.lives, 1)
        self.assertEqual(vampyre.hit_points, 3)

        vampyre.take_damage(damage=18)
        self.assertEqual(vampyre.lives, 0)
        self.assertEqual(vampyre.hit_points, 0)

        vampyre.take_damage(damage=1)
        self.assertEqual(vampyre.lives, 0)
        self.assertEqual(vampyre.hit_points, 0)

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
