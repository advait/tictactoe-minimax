"""Dead simple tic-tac-toe minimax experiment."""

import math
from typing import List, Tuple

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
lines = [row0, row1, row2, col0, col1, col2, diag0, diag1]


def score_board(b: Board) -> Score:
    """Returns Inf if X has won, -Inf if O has won, Zero otherwise"""
    for line in lines:
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
    scored_moves = []
    for move in enumerate_moves(b, p):
        # Recursively use minimax to score the potential moves
        score, _ = minimax(move, next_player(p))
        scored_moves.append((score, move))
    if not scored_moves:
        return score_board(b), b  # No positions left
    value_f = max if p == "X" else min  # How to value the possible moves (min or max)
    # If you want more randomness, select randomly between moves that have the same apparent score
    return value_f(scored_moves)


def print_board(b: Board):
    """Prints a formatted board"""
    print("%s|%s|%s\n-+-+-\n%s|%s|%s\n-+-+-\n%s|%s|%s\n" % b)


def prompt_move(b: Board, p: Player) -> Board:
    """Prompts a human player for a move and returns the resulting board."""
    i = int(input("%s's turn. Please enter a position from 0 through 9: " % p))
    if b[i] != " ":
        print("Invalid move")
        return prompt_move(b, p)
    return play_move(b, p, i)


def main():
    b = (" ",) * 9  # Empty board
    print_board(b)

    while True:
        # Player's turn
        b = prompt_move(b, "X")
        print_board(b)
        if game_over(b):
            print("Game Over")
            return
        # Computer's turn
        s, b = minimax(b, "O")
        print_board(b)
        if game_over(b):
            print("Game Over")
            return


if __name__ == "__main__":
    main()
