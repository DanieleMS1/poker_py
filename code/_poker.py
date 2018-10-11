# NO FUNCTIONS IN HERE
# ONLY FOR TESTING THE GAME

from blinds_and_bets import *
from game_creation import *
from Player import *
from winning_and_showdown import *

# SETUP

listw = []


def round(players):
    sb = 10
    bb = 2 * sb
    deck = create_deck()
    board = create_board()
    pot = create_pot()
    display_all_players(players)
    put_blinds_in_pot(players, sb, bb, pot)
    deal(players, deck)
    flop(deck, board)
    turn_river(deck, board)
    turn_river(deck, board)
    winning_hands = best_hands(players, board)
    winners = find_winners(players, winning_hands)
    for i, player in enumerate(players):
        bet(i, players, 100, pot)
    give_money_to_winners(winners, players, pot)
    pot = create_pot()

    for player in players:
        check_enough_money(player, players)
    if check_if_game_over(players):
        return
    rotate_buttons(players)

def game():
    players = create_players(3)
    start_buttons(players)
    for i in range(5000):
        round(players)
        print('\n')
        if check_if_game_over(players):
            # for player in players:
            #     listw.append(player.name)
            break

game()
#
# for n in range(60):
#     game()
#
#
# listw.sort()
#
# dictwin = {}
#
# for i in listw:
#     if i not in dictwin:
#         dictwin[i] = 0
#     else:
#         dictwin[i] += 1
#
# print(dictwin)
