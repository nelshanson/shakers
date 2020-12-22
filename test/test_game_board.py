from shakers.game import GameBoard

# Test some small-scale games. This isn't exactly comprehensive at
# this point.

def test_sample_game():
    dims = (3, 3)
    board = [
        ['R', '-', 'D'],
        ['-', '#', '-'],
        ['R', '#', 'U']
    ]
    game = GameBoard(dims, board)
    assert game.play() == 2

def test_no_handshakes():
    dims = (3, 3)
    board = [
        ['U', '-', 'U'],
        ['-', '#', '-'],
        ['L', '#', 'D']
    ]
    game = GameBoard(dims, board)
    assert game.play() == 0

def test_no_handshakes_because_of_traps():
    dims = (3, 3)
    board = [
        ['R', '#', 'L'],
        ['-', '#', '-'],
        ['R', '#', 'L']
    ]
    game = GameBoard(dims, board)
    assert game.play() == 0

def test_board_with_triple_meeting_and_multiple_meeting_per_person():
    dims = (3, 3)
    board = [
        ['R', '-', 'L'],
        ['-', 'U', '-'],
        ['U', '-', 'U']
    ]
    game = GameBoard(dims, board)
    assert game.play() == 5