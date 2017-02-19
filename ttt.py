#!/usr/bin/env python3
"""Dead simple tic-tac-toe minimax experiment."""

import itertools
import math
import random
from typing import List, Tuple

# Type definitions
# X, O, or space
Square = str
# X, O
Player = str
# Minimax score
Score = float
# Immutable tuple of Squares
Board = Tuple[Square, Square, Square, Square, Square, Square, Square, Square, Square]

# Indexes of all the rows, cols, and diags
row0 = (0, 1, 2)
row1 = (3, 4, 5)
row2 = (6, 7, 8)
col0 = (0, 3, 6)
col1 = (1, 4, 7)
col2 = (2, 5, 8)
diag0 = (0, 4, 8)
diag1 = (2, 4, 6)
all_lines = [row0, row1, row2, col0, col1, col2, diag0, diag1]


def score_board(b: Board) -> Score:
    """Returns Inf if X has won, -Inf if O has won, Zero otherwise"""
    for line in all_lines:
        s = "".join(b[i] for i in line)  # Concise representation of line
        if s == "XXX":
            return math.inf
        elif s == "OOO":
            return -math.inf
    return 0


def game_over(b: Board) -> bool:
    """Returns whether a players has won or there are no moves left."""
    if score_board(b) != 0:
        return True
    for s in b:
        if s == " ":
            return False
    return True


def play_move(b: Board, p: Player, i: int) -> Board:
    """Returns a new board where the i'th position is played by p."""
    return b[:i] + (p,) + b[i + 1:]


def enumerate_moves(b: Board, p: Player) -> List[Board]:
    """Enumerates all the possible moves that player to_play can make."""
    return [play_move(b, p, i) for i, square in enumerate(b) if square == " "]


def next_player(p: Player) -> Player:
    """Returns the next player to play."""
    return "X" if p == "O" else "O"


def minimax(b: Board, p: Player) -> (Score, Board):
    """Returns a move and the corresponding score using minimax."""
    if game_over(b):
        return score_board(b), b  # No positions left
    scored_moves = []
    for move in enumerate_moves(b, p):
        # Recursively use minimax to score the potential moves
        score, _ = minimax(move, next_player(p))
        scored_moves.append((score, move))
    value_f = max if p == "X" else min  # How to value the possible moves (min or max)
    # Randomly select a move with best score (so we get more randomness, instead of always choosing the last move)
    best_score, _ = value_f(scored_moves)
    return random.choice([(score, move) for (score, move) in scored_moves if score == best_score])


def print_board(b: Board):
    """Prints a formatted board"""
    print("%s|%s|%s\n-+-+-\n%s|%s|%s\n-+-+-\n%s|%s|%s\n" % b)


def human_move(b: Board, p: Player = "X") -> Board:
    """Prompts a human player for a move and returns the resulting board."""
    i = int(input("%s's turn. Please enter a position from 0 through 9: " % p))
    print("")
    if b[i] != " ":
        print("Invalid move")
        return human_move(b, p)
    return play_move(b, p, i)


def computer_move(b: Board, p: Player = "O") -> Board:
    """Plays a computer's turn using minimax and returns the resulting board."""
    print("Computer's turn. Thinking...\n")
    _, b = minimax(b, p)
    return b


def main():
    b = (" ",) * 9  # Empty board
    print_board(b)

    play_funs = [human_move, computer_move]
    random.shuffle(play_funs)  # Randomly choose human or computer first
    alternating = itertools.cycle(play_funs)  # Infinite cycle between both human/computer
    while True:
        play_fun = next(alternating)
        b = play_fun(b)
        print_board(b)
        if game_over(b):
            print("Game Over")
            return

if __name__ == "__main__":
    main()
