from .parser import parse_game_file
from .game import GameBoard

import sys

def _main():
    filename = sys.argv[1]
    dims, rows = parse_game_file(filename)
    g = GameBoard(dims, rows)
    return g.play()
