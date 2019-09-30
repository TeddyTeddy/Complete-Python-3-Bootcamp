from player import Player
from enemy import Enemy, Troll, Vampyre

tim = Player('Tim')

random_monster = Enemy('Basic Enemy', 12, 1)
print(random_monster)
random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

random_monster.take_damage(9)
print(random_monster)

ugly_troll = Troll('Pug')  # note that it takes no arguments. Calls Enemy.__init__
print('Ugly troll - {}'.format(ugly_troll))

another_troll = Troll('Ug')  # note that it takes 3 arguments. Calls Enemy.__init__
print(f'Another troll {another_troll}')

brother_troll = Troll('Urg')  # note that it takes 2 arguments. Calls Enemy.__init__
print(f'Brother troll {brother_troll}')

ugly_troll.grunt()
another_troll.grunt()
brother_troll.grunt()

ugly_troll.take_damage(23)
print(ugly_troll)
ugly_troll.take_damage(1)
print(ugly_troll)
ugly_troll.take_damage(1)
print(ugly_troll)

drakula = Vampyre('Drakula')
print(drakula)
drakula.take_damage(50)
print(drakula)
drakula.take_damage(8)
print(drakula)
drakula.take_damage(15)
print(drakula)
drakula.take_damage(15)
print(drakula)

#
# print(tim.name)
# print(tim.lives)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# print('\nSetting different levels to the player Tim')
# print(tim)
# tim.level = -1000
# print('\ntim.level = -1000\n',tim)
# tim.level -= 100
# print('\ntim.level -= 100\n', tim)
# tim.level = 0
# print('\ntim.level = 0\n', tim)
# tim.level = 1
# print('\ntim.level = 1\n', tim)
# tim.level += 3
# print('\ntim.level += 3\n', tim)
# tim.level += 5
# print('\ntim.level += 5\n', tim)
# tim.level -= 100
# print('\ntim.level -= 100\n', tim)
#
# tim.score = 500
# print(tim)


