from shakers.parser import parse_game_file

def test_parses_game_file_correctly():
    dims, board = parse_game_file("test/test_board.txt")
    assert dims == (3, 3)
    assert board == [
        ['R', '-', 'D'],
        ['-', '#', '-'],
        ['R', '#', 'U']
    ]