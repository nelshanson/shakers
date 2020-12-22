from shakers.game import Person

def test_move_person_up():
    p = Person('U', 0, 0)
    p.move()
    assert p.coords == (-1, 0)

def test_move_person_down():
    p = Person('D', 0, 0)
    p.move()
    assert p.coords == (1, 0)

def test_move_person_left():
    p = Person('L', 0, 0)
    p.move()
    assert p.coords == (0, -1)

def test_move_person_right():
    p = Person('R', 0, 0)
    p.move()
    assert p.coords == (0, 1)
