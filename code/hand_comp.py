from itertools import combinations


def poker(hands):
    "Return a list of the winning hands"
    return all_max(hands, key=hand_rank)


def all_max(iterable, key=None):
    "Max() that returns all the values that are max"
    result = []
    max_value = None
    key = key or (lambda x: x)
    for x in iterable:
        x_val = key(x)
        if not result or x_val > max_value:
            result = [x]
            max_value = x_val
        elif x_val == max_value:
            result.append(x)
    return result


def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first"
    ranks = ['--23456789TJQKA'.index(r) for r, s in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight"
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
    "Return true if all cards have the same suit"
    suits = [s for r, s in hand]
    return len(set(suits)) == 1


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of"""
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks):
    "Return rank of the 2 pair if not returns None"
    high_pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if high_pair and low_pair != high_pair:
        return (high_pair, low_pair)
    return None


def hand_rank(hand):
    "Return a value indicating the ranking of a hand"
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    if kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    if kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    if flush(hand):
        return (5, ranks)
    if straight(ranks):
        return (4, max(ranks))
    if kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    if two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    if kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    return (0, ranks)


def hands_holdem(hand, board, hand_size=5):
    "Return every 5-card hand from 7"
    hand_plus_board = hand + board
    every_hand = list(combinations(hand_plus_board, hand_size))
    return every_hand
