from typing import List, Tuple
from .person import Person

class GameBoard:

    def __init__(self, dims: Tuple[int, int], board: List[List[str]]):
        self._hand_shakes = 0
        self._x_max = dims[0]
        self._y_max = dims[1]

        traps, people = _process_initial_board_state(dims, board)
        self._traps = traps
        self._people = people


    def _process_initial_board_state(dims, board):
        n, m = dims
        traps = set()
        people = set()

        for i in range(n):
            for j in range(m):
                char = board[i][j]
                if char == '#':
                    traps.add((i, j))
                elif char == '-':
                    continue
                else:
                    people.add(Person(char, i, j))

        return traps, people
