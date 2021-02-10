import bs4
import requests
from botLogic import BotLogic
from People import PlayerLogic


def ships_create_change_values_game():
    bot = BotLogic()
    player = PlayerLogic()
    bot.ships_create()
    player.ships_create()
    change_game = bot.game
    change_ships_dots = bot.ship_dots
    change_border_dots = bot.border_dots
    change_hp = bot.hp
    bot.set_game(player.game)
    bot.set_ship_dots(player.ship_dots)
    bot.set_border_dots(player.border_dots)
    bot.set_hp(player.hp)
    player.set_game(change_game)
    player.set_ship_dots(change_ships_dots)
    player.set_border_dots(change_border_dots)
    player.set_hp(change_hp)
    game(bot, player)
    return


def game(bot, player):
    while True:
        win = bot.turn()
        if win:
            break
        win = player.turn()
        if win:
            break


ships_create_change_values_game()
