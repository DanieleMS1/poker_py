from random import shuffle, randint

from Player import *

# BLINDS------------------------------------------------------------------------


def start_buttons(list_of_players):
    "Gives the buttons"
    n_of_p = len(list_of_players) - 1
    start_sb = randint(0, n_of_p)
    if start_sb == n_of_p:
        start_bb = 0
    else:
        start_bb = start_sb + 1
    list_of_players[start_sb].sb = 'SB'
    list_of_players[start_bb].bb = 'BB'


def put_blinds_in_pot(list_of_players, pot):
    "Puts the blinds in the pot"
    sb_bet = 10
    sb_player = search_for_sb(list_of_players)
    bb_player = search_for_bb(list_of_players)
    bet(sb_player, list_of_players, sb_bet, pot)
    bet(bb_player, list_of_players, 2 * sb_bet, pot)


def search_for_sb(list_of_players):
    "Searches for the small blind"
    for i, player in enumerate(list_of_players):
        if player.sb == 'SB':
            return i


def search_for_bb(list_of_players):
    "Searches for the big blind"
    for i, player in enumerate(list_of_players):
        if player.bb == 'BB':
            return i


def search_for_player_before_sb(list_of_players):
    "Searches for the player before the small blind"
    n_of_p = len(list_of_players) - 1
    sb_player = search_for_sb(list_of_players)
    if sb_player == 0:
        return n_of_p
    return sb_player - 1


def put_blinds_in_pot(list_of_players, ammount_sb, ammount_bb, pot):
    "SB and BB put the blinds in the pot"
    player_sb = search_for_sb(list_of_players)
    player_bb = search_for_bb(list_of_players)
    bet(player_sb, list_of_players, ammount_sb, pot)
    bet(player_bb, list_of_players, ammount_bb, pot)


def rotate_buttons(list_of_players):
    "Shifts the blinds clockwise ''->SB, SB->BB, BB->'' "
    prev_player = search_for_player_before_sb(list_of_players)
    sb_player = search_for_sb(list_of_players)
    bb_player = search_for_bb(list_of_players)

    for player in [sb_player, bb_player]:
        list_of_players[player].sb = ''
        list_of_players[player].bb = ''

    list_of_players[prev_player].sb = 'SB'
    list_of_players[sb_player].bb = 'BB'

# BETS--------------------------------------------------------------------------


def bet(player, list_of_players, bet, pot):
    "Moves money from the player to the pot and takes notice of who bet"
    if not all_in(player, list_of_players, bet):
        list_of_players[player].money -= bet
        pot["Tot"] += bet
    else:
        bet = list_of_players[player].money
        list_of_players[player].money = 0
        pot["Tot"] += bet
    bet_tracker(player, bet, pot)


def bet_tracker(player, bet, pot):
    "Tracks the bets that each player made"
    if not (player in pot):
        pot[player] = bet
    else:
        pot[player] += bet


def check_enough_money(player, list_of_players):
    "Kicks the player with no money"
    if player.money == 0:
        if player.sb != '':
            rotate_buttons(list_of_players)
            rotate_buttons(list_of_players)
        if player.bb != '':
            rotate_buttons(list_of_players)
        del list_of_players[list_of_players.index(player)]


def all_in(player, list_of_players, bet):
    "Checks if the bet is more than the money the player has"
    return False if bet < list_of_players[player].money else True


def fold(player, list_of_players):
    "Ask the player if he wants to fold"
    check = input("Player {} Would you like to fold ? : [Y/N]".format(player))
    if check.lower() == 'y':
        del list_of_players[player]


def empty_bets_in_pot(pot, list_of_players):
    "Resets the pot"
    for player in list_of_players:
        if player in pot:
            del pot[player]
