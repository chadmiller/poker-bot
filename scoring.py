#!/usr/bin/python3

# sprint discussion with FanJun

import re

def score_hand(cards):
    """
    >>> score_hand(["as", "5c", "3d", "1d", "qh"])
    (..., 'nothing')
    >>> score_hand(["ks", "ts", "js", "qs", "as"])
    (..., 'straight royal flush')
    >>> score_hand(["ks", "tc", "jd", "qd", "9h"])
    (..., 'straight')
    >>> score_hand(["2s", "2c", "3s", "3d", "3h"])
    (..., 'full house')
    >>> score_hand(["2s", "2c", "2d", "3s", "3d"])
    (..., 'full house')
    >>> score_hand(["2s", "9s", "3s", "ts", "7s"])
    (..., 'flush')
    >>> score_hand(["2h", "2d", "2s", "2c", "9s"])
    (..., 'four of a kind')
    >>> score_hand(["2c", "2s", "3s", "3s", "9s"])
    (..., 'two pair')
    >>> score_hand(["2c", "2s", "as", "3s", "3s"])
    (..., 'two pair')
    >>> score_hand(["2c", "2s", "5s", "7s", "9s"])
    (..., 'pair')
    >>> score_hand(["2c", "2s", "2s", "7s", "9s"])
    (..., 'three of a kind')
    """

    cardval = { "t": 10, "j": 11, "q": 12, "k": 13, "a": 14 }

    score = 0
    description = []

    cards.sort()
    cards_str = " ".join(cards)

    if re.search(r"(.). \1. \1. \1.", cards_str):
        score = 41640
        description.append("four of a kind")

    elif re.search(r"(.). \1. \1. (.). \2.", cards_str):
        score = 6930
        description.append("full house")

    elif re.search(r"(.). \1. (.). \2. \2.", cards_str):
        score = 6930
        description.append("full house")

    elif re.search(r"(.). \1. \1.", cards_str):
        score = 463
        description.append("three of a kind")

    elif re.search(r"(.). \1. .. (.). \2", cards_str):
        score = 200
        description.append("two pair")

    elif re.search(r"(.). \1. (.). \2.", cards_str):
        score = 200
        description.append("two pair")

    elif re.search(r"(.). \1.", cards_str):
        score = 14
        description.append("pair")

    # straights are hard
    vals = list(sorted(int(cardval.get(c[0], c[0])) for c in cards))
    if vals == list(range(vals[0], vals[4]+1)):
        score = 2540
        description.append("straight")

    if re.match(r".(.) .\1 .\1 .\1 .\1", cards_str):
        if description == ["straight"]:
            if any(c.startswith("a") for c in cards):
                description.append("royal")
                score = 6497390
            else:
                score = 721920
        else:
            score = 5080
        description.append("flush")

    # bottom case, sum of cards
    score += sum(int(cardval.get(c[0], c[0])) for c in cards) / 500.0
    return score, " ".join(description) if description else "nothing"


import doctest
doctest.testmod(optionflags=doctest.ELLIPSIS)
