# The example function below keeps track of the opponent's history
# and plays whatever the opponent played two plays ago.
# It is not a very good player so you will need to change
# the code to pass the challenge.
from typing import Literal
from random import choice

Hand = Literal["R", "P", "S", ""]


def player(prev_play: Hand, opponent_history: list[Hand] = []) -> Hand:
    return ""


def oneMemoryPlayer(prev_play: Hand, opponent_history: list[Hand] = []) -> Hand:
    """
    simply try to beat the opponent's hand just before
    Its scores are: 50, 50, 84, 100
    """
    opponent_history.append(prev_play)
    guess = opponent_history[-1]
    return oppose(guess)


def oppose(hand: Hand) -> Hand:
    """ "
    When given a hand, return the winning hand
    """
    if hand == "P":
        return "S"
    elif hand == "R":
        return "P"
    elif hand == "S":
        return "R"
    return choice(["R", "P", "S"])
