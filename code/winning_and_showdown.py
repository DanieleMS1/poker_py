from random import shuffle, randint

from blinds_and_bets import empty_bets_in_pot
from hand_comp import *
from Player import *


def best_hands(list_of_players, board):
    "Given a board and the hands of the players figures out the best hand(s)"
    all_best_hands = []
    for player in list_of_players:
        player_hands = hands_holdem(player.hand, board)
        best_player_hands = poker(player_hands)
        all_best_hands += best_player_hands
    winning_hands = poker(all_best_hands)
    return list(set(winning_hands))


def find_winners(list_of_players, winning_hands):
    "Finds the winners and returns them"
    winners = []
    for player in list_of_players:
        for card in player.hand:
            for hand in winning_hands:
                if card in hand:
                    winners.append(player.name)
    return sorted(list(set(winners))) if winners else [player.name for player in list_of_players]


def showdown(list_of_players, winning_hands):
    "Prints out the best hand(s) and the winner(s)"
    return([winning_hands, find_winners(list_of_players, winning_hands)])


def give_money_to_winners(list_of_winners, list_of_players, pot):
    "Gives the money to the winners"
    split = pot["Tot"] / len(list_of_winners)
    for winner in list_of_winners:
        pot["Tot"] -= split
        for i, player in enumerate(list_of_players):
            if player.name == winner:
                index_of_winner = i
                break
        list_of_players[index_of_winner].money += split
    empty_bets_in_pot(pot, list_of_players)
