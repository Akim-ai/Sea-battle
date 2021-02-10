import bs4
import requests


class Ship:
    def __init__(self):
        self.lensPrint = [3, 2, 2, 1, 1, 1, 1]
        self.hp = []
        self.dots = []
        self.game = [[' ', '|', '1', '|', '2', '|', '3', '|', '4', '|', '5', '|', '6'],
                     ['1', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O'],
                     ['2', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O'],
                     ['3', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O'],
                     ['4', '|', 'O', '|', 'O', '|', '0', '|', 'O', '|', 'O', '|', 'O'],
                     ['5', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O'],
                     ['6', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O']]

        self.border_dots = []
        self.border_x_left = [[-1, -2], [0, -2], [1, -2]]
        self.border_x_middle = [[-1, 0], [1, 0]]
        self.border_x_right = [[-1, 2], [0, 2], [1, 2]]

        self.border_y_up = [[-1, -2], [-1, 0], [-1, 2]]
        self.border_y_middle = [[0, -2], [0, 2]]
        self.border_y_down = [[1, -2], [1, 0], [1, 2]]

    def get_dots(self):
        return self.dots

    def get_border_dots(self):
        return self.border_dots

    def ships_start(self):
        print('Что же, сейчас подготовительная часть игры, нужно разместить корабли.\n'
              'Как же это происходит? Вы выбераете ось (0/1 = X/Y) написав цифорку \n'
              'после чего длину корабля и потом координаты на которых хотите разместить\n'
              'ваш прекрасный корабль. А что дальше? Разберётесь)\n\nЧтож, приступим.')
        self.ships_create_player()
        return self.game, self.dots, self.border_dots, self.hp

    def ships_create_player(self):
        while self.lensPrint:
            for i in range(0, 7):
                print(self.game[i][0], self.game[i][1], self.game[i][2], self.game[i][3], self.game[i][4],
                      self.game[i][5], self.game[i][6], self.game[i][7], self.game[i][8], self.game[i][9],
                      self.game[i][10], self.game[i][11], self.game[i][12])
            dots_xy = []
            print("Сейчас вы можете разместить корабли с длинами: ")
            print(self.lensPrint)
            try:
                lens_hp = int(input('Какой будем кидать на доску?'))
                if 1 < lens_hp:
                    x_y = int(input('Разметим корабль по вертикали или горизонтали?(0/1) '))
                else:
                    x_y = 0
                dots_x = int(input('Ось Х: '))
                dots_y = int(input('Ось Y: ')) * 2
            except ValueError:
                print('\n\nСтоит придерживаться правил игры.\n\n')
                return self.ships_create_player()
            if lens_hp in self.lensPrint:
                if x_y:
                    if ((12 < dots_y + lens_hp * 2 - 2) or (6 < dots_x)) or \
                            (dots_y <= 0 or dots_x <= 0):
                        print('\n\nЯ понимаю что разместив корабль за доской бот по нему'
                              ' не попадёт, но мы это предусмотрели!;D\n\n ')
                        return self.ships_create_player()
                elif ((12 < dots_y) or (6 < dots_x + lens_hp - 1)) or \
                        (dots_y <= 0 or dots_x <= 0):
                    print('\n\nЯ понимаю что разместив корабль за доской бот по нему'
                          ' не попадёт, но мы это предусмотрели!;D\n\n ')
                    return self.ships_create_player()
                dots_xy.append(dots_x)
                dots_xy.append(dots_y)
                for i in self.dots:
                    if dots_xy in i:
                        print('\n\nПо таким координатам уже размещён корабль.\n\n')
                        return self.ships_create_player()
                dots_xy.append(dots_x)
                dots_xy.append(dots_y)
                self.ship_border(x_y, lens_hp, dots_xy)
                for i in self.dots[-1]:
                    self.game[i[0]][i[1]] = '■'
                count = 0
                place = 0
                not_repeated = []
                for i in self.dots:
                    for j in self.dots[place]:
                        count += 1
                    for j in self.border_dots[place]:
                        if j not in not_repeated:
                            not_repeated.append(j)
                            count += 1
                    place += 1
                if 35 < count:
                    print('\n\nПрийдётся начать размещение заного, на доске не осталось места\n\n')
                    self = Ship()
                    return self.ships_create_player()

            else:
                print('\n\nКорабля с длиной ', str(lens_hp), ' нет в наличии.\n\n')
                return self.ships_create_player()
        return self.game, self.dots, self.border_dots, self.hp

    def ship_border(self, x_y, lens_hp, dots_xy, turn=1):
        list_before_append = []
        dots = []
        if x_y == 1:
            for i in range(0, 3):
                list_before_append.append([dots_xy[0] + self.border_x_left[i][0],
                                           dots_xy[1] + self.border_x_left[i][1]])
                list_before_append.append([dots_xy[0] + self.border_x_right[i][0],
                                           dots_xy[1] + lens_hp * 2])
            for i in range(0, lens_hp):
                list_before_append.append([dots_xy[0] + self.border_x_middle[0][0],
                                           dots_xy[1] + i * 2 + self.border_x_middle[0][1]])
                list_before_append.append([dots_xy[0] + self.border_x_middle[1][0],
                                           dots_xy[1] + i * 2 + self.border_x_middle[1][1]])
                dots.append([dots_xy[0], dots_xy[1] + i * 2])
        else:
            for i in range(0, 3):
                list_before_append.append([dots_xy[0] + self.border_y_up[i][0],
                                           dots_xy[1] + self.border_y_up[i][1]])
                list_before_append.append([dots_xy[0] + self.border_y_down[i][0] + lens_hp - 1,
                                           dots_xy[1] + self.border_y_down[i][1]])
            for i in range(0, lens_hp):
                list_before_append.append([dots_xy[0] + self.border_y_middle[0][0] + i,
                                           dots_xy[1] + self.border_y_middle[0][1]])
                list_before_append.append([dots_xy[0] + self.border_y_middle[1][0] + i,
                                           dots_xy[1] + self.border_y_middle[1][1]])
                dots.append([dots_xy[0] + i, dots_xy[1]])
        a = []
        for i in list_before_append:
            if 7 <= i[0] or i[0] <= 0:
                a.append(i)
            elif 14 <= i[1] or i[1] <= 0:
                a.append(i)
        for i in a:
            list_before_append.remove(i)
        count_border_dots = 0
        for i in self.border_dots:
            count_border_dots += 1
        for i in dots:
            for j in range(0, count_border_dots):
                if i in self.border_dots[j]:
                    if turn:
                        print('\n\nМы не можем позволить такую близость среди кораблей\n\n')
                        return self.ships_create_player()
                    else:
                        self.hp = []
                        self.dots = []
                        self.border_dots = []
                        return self, [], []
        if turn:
            self.lensPrint.remove(lens_hp)
        self.hp.append(lens_hp)
        self.dots.append(dots)
        self.border_dots.append(list_before_append)
        if turn:
            return
        else:
            return list_before_append, self.dots[-1]
