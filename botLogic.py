import bs4
import requests
import random
from ships import Ship


class BotLogic:
    def __init__(self):
        self.steps = []
        self.left = 0
        self.got = 0
        self.game = [[' ', '|', '1', '|', '2', '|', '3', '|', '4', '|', '5', '|', '6'],
                     ['1', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O'],
                     ['2', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O'],
                     ['3', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O'],
                     ['4', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O'],
                     ['5', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O'],
                     ['6', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O']]
        self.ship_dots = []
        self.border_dots = []
        self.hp = []

    def ships_create(self):
        try:
            self.steps_create()
            bot_ship = Ship()
            self.ship_dots = []
            self.border_dots = []
            for i in bot_ship.lensPrint:
                count = 0
                while True:
                    dots = random.randint(0, self.left)
                    x_y = random.randint(0, 1)
                    dots = self.steps[dots]
                    if (dots[1] + i * 2 - 2) <= 12 and dots[0]+i-1 < 7:
                        border_dots_remove, last_ship_dots = bot_ship.ship_border(x_y, i, dots, 0)
                        if border_dots_remove:
                            for j in border_dots_remove:
                                if j in self.steps:
                                    self.steps.remove(j)
                                    count += 1
                            for j in last_ship_dots:
                                if j in self.steps:
                                    self.steps.remove(j)
                                    count += 1
                            self.left -= count
                            break
            self.ship_dots = bot_ship.dots
            self.border_dots = bot_ship.border_dots
            self.hp = bot_ship.hp
            self.steps_create()
            return self
        except ValueError or IndexError or RecursionError:
            self.ships_create()

    def steps_create(self):
        self.left = 35
        self.steps = []
        for i in range(1, 7):
            for j in range(1, 7):
                self.steps.append([i, j*2])

    def get_values(self):
        return self.game

    def set_values(self, game, ship_dots, border_dots, hp):
        self.set_game(game)
        self.set_ship_dots(ship_dots)
        self.set_border_dots(border_dots)
        self.set_hp(hp)
        return

    def set_game(self, game):
        self.game = game

    def set_ship_dots(self, ship_dots):
        self.ship_dots = ship_dots

    def set_border_dots(self, border_dots):
        self.border_dots = border_dots

    def set_hp(self, hp):
        self.hp = hp

    def turn(self):
        dots = random.randint(0, self.left)
        dots = self.steps.pop(dots)
        self.left -= 1
        count = 0
        if self.game[dots[0]][dots[1]] == '■':
            self.game[dots[0]][dots[1]] = 'X'
            for i in self.ship_dots:
                if dots in i:
                    self.hp[count] -= 1
                    if self.hp[count] == 0:
                        self.ship_dots.remove(i)
                        self.hp.remove(self.hp[count])
                        for j in self.border_dots[count]:
                            self.game[j[0]][j[1]] = '.'
                        self.border_dots.remove(self.border_dots[count])
                    self.game_print()
                    if self.hp:
                        return self.turn()
                    else:
                        print('Bot "Random" победил в этом противостояние!')
                        return True
                count += 1
        elif self.game[dots[0]][dots[1]] == 'O':
            self.game[dots[0]][dots[1]] = 'T'
            self.game_print()
            return False
        else:
            return self.turn()

    def game_print(self):
        for i in range(0, 7):
            print(self.game[i][0], self.game[i][1], self.game[i][2], self.game[i][3], self.game[i][4],
                  self.game[i][5], self.game[i][6], self.game[i][7], self.game[i][8], self.game[i][9],
                  self.game[i][10], self.game[i][11], self.game[i][12])
        print('')
