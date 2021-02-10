import bs4
import requests
from ships import Ship


class PlayerLogic:
    def __init__(self):
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

    def get_game(self):
        return self.game

    def give_values(self):
        return self.game, self.ship_dots, self.border_dots, self.hp

    def set_game(self, game):
        self.game = game

    def set_ship_dots(self, ship_dots):
        self.ship_dots = ship_dots

    def set_border_dots(self, border_dots):
        self.border_dots = border_dots

    def set_hp(self, hp):
        self.hp = hp

    def ships_create(self):
        ships = Ship()
        self.game, self.ship_dots, self.border_dots, self.hp = ships.ships_start()

    def set_values(self, game, ship_dots, border_dots, hp):
        self.set_game(game)
        self.set_ship_dots(ship_dots)
        self.set_border_dots(border_dots)
        self.set_hp(hp)

    def turn(self):
        try:
            self.game_print()
            x = int(input('Горизонталь: '))
            y = (int(input('Вертикаль: '))) * 2
            dots = [x, y]
            self.game_print()
        except ValueError:
            print('\n\nПоле 6 на 6, возвращаемся...\n\n')
            return self.turn()
        count = 0
        if 0 < x < 7 and 0 < y < 13:
            for i in self.ship_dots:
                if dots in i:
                    self.hp[count] -= 1
                    if 1 < self.hp[count]:
                        self.ship_dots[count].remove(dots)
                        print('\n\nЕсть Попадание! Продолжаем.')
                    self.game[x][y] = 'X'
                    if self.hp[count] == 0:
                        self.ship_dots.remove(i)
                        self.hp.remove(self.hp[count])
                        for j in self.border_dots[count]:
                            self.game[j[0]][j[1]] = '.'
                        self.border_dots.remove(self.border_dots[count])
                        print('Смэрт!')
                    if self.hp:
                        return self.turn()
                    else:
                        self.game_print()
                        print('Люди оказались сильнее машин!')
                        return True
                count += 1
            if self.game[x][y] == 'T':
                print('\n\nТут ничего нет, ты даже проверил это...\n\n')
                return self.turn()
            elif self.game[x][y] == 'X':
                print('\n\nНа этом месте и так труп, зачем ты его пинаешь?\n\n')
                return self.turn()
            elif self.game[x][y] == '.':
                print('\n\nТут уж точно ничего быть не может...\n\n')
                return self.turn()
            else:
                print('Промашка.')
                self.game[x][y] = 'T'
                return False
        else:
            print('\n\nПоле 6 на 6...\n\n')
            return self.turn()

    def game_print(self):
        for i in range(0, 7):
            print(self.game[i][0], self.game[i][1], self.game[i][2], self.game[i][3], self.game[i][4],
                  self.game[i][5], self.game[i][6], self.game[i][7], self.game[i][8], self.game[i][9],
                  self.game[i][10], self.game[i][11], self.game[i][12])
