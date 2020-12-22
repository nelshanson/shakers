from .game import GameBoard

DIRECTIONS = set(['D', 'U', 'R', 'L'])

def parse_game_file(filename):
    """Parse the contents of a game file to a game board"""
    with open(filename, 'r') as f:
        rows = []
        i, j = f.readline().strip().split()
        for line in f.readlines():
            rows.append(list(line.strip()))

    return (int(i), int(j)), rows
