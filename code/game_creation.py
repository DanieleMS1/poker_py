from random import shuffle, randint

from Player import *


def create_players(n):
    "Creates a list of players : [hands, money, button]"
    list_of_players = []
    for i in range(n):
        list_of_players.append(Player(i))
    return list_of_players


def create_deck(n_decks=1):
    "Creates a standard deck"
    suits = ['♥', '♦', '♣', '♠']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']
    deck = [str(v) + s for s in suits for v in values]
    deck *= n_decks
    return deck


def create_board():
    "Creates the board"
    board = []
    return board


def create_pot():
    "Creates the pot"
    pot = {
        "Tot": 0.0
    }
    return pot


def deal(list_of_players, deck, n=2):
    "Shuffles the deck and deals n cards to the players"
    shuffle(deck)
    for player in list_of_players:
        player.hand = deck[:n]
        del deck[:n]
    return list_of_players


def burn(deck):
    "Burns 1 card from the top of the deck"
    del deck[:1]


def flop(deck, board, n=3):
    "Burns 1 card and appends 3 to the board"
    burn(deck)
    board += deck[:n]
    del deck[:n]


def turn_river(deck, board, n=1):
    "Burns 1 card and appends 1 to the board"
    burn(deck)
    board += deck[:n]
    del deck[:n]


def display_all_players(list_of_players):
    "Displays all the players"
    display_list = [player.display() for player in list_of_players]
    print(display_list)


def check_if_game_over(list_of_players):
    "if there is only one player returns True"
    return True if len(list_of_players) < 2 else False
