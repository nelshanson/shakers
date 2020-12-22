from typing import List, Tuple
from collections import defaultdict
from .person import Person

class GameBoard:

    def __init__(self, dims: Tuple[int, int], board: List[List[str]]):
        self._hand_shakes = 0
        self._x_max = dims[0]
        self._y_max = dims[1]

        traps, people = self._process_initial_board_state(dims, board)
        self._traps = traps
        self._people = people


    def _process_initial_board_state(self, dims, board):
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

    def _play_round(self):
        # Move each player
        print(self._people)
        [person.move() for person in self._people]
        print(self._people)

        # Sweep up out of bounds and trapped people
        self._sweep()

        # Count up any handshakes to be had.
        return self._count_handshakes()


    def _sweep(self):
        remove = set()

        for person in self._people:
            if person.coords in self._traps or self._out_of_bounds(person):
                remove.add(person)

        self._people.difference_update(remove)

    def _count_handshakes(self):
        handshakes = 0
        meetings = defaultdict(int)

        for person in self._people:
            meetings[person.coords] += 1
        
        for k, v in meetings.items():
            if v > 1:
                handshakes += v*(v-1)/2
        
        return handshakes

    def _out_of_bounds(self, person):
        i, j = person.coords
        return i < 0 or j < 0 or i >= self._x_max or j >= self._y_max

    def play(self):
        handshakes = 0
        while len(self._people) > 0:
            handshakes += self._play_round()
        return handshakes