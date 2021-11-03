import random

from pytest import mark


def point(center, r, point):
    """
    Дана точка center - пара (x, y) и целый радиус r, а также точка point - тоже две координаты
    Вернуть True, если point лежит в круге с центром center и радиусом r, и False иначе

    point((0, 2), 3, (0, 0)) :returns True
    """
    pass


@mark.parametrize('data', [
    [(0, 0), 1, (1, 0), True],
    [(1, 0), 2, (0, -1), True],
    [(1, 0), 2, (0, -2), False],
    [(3, 4), 5, (0, 0), True],
    [(3, 3), 10, (-5, 9), True],
    [(3, 3), 10, (-6, 7), True],
    [(3, 3), 10, (-6, 8), False],
    [(3, 3), 8, (-6, 7), False],
])
def test_point(data):
    assert point(data[0], data[1], data[2]) == data[3]


@mark.parametrize('seed', list(range(20)))
def test_randomized(seed):
    random.seed(seed)
    cx, cy = random.randint(-1000, 1000), random.randint(-1000, 1000)
    px, py = random.randint(-1000, 1000), random.randint(-1000, 1000)
    r = ((px + py) ** 2 - 2 * px * py) ** 0.5
    px += cx
    py += cy
    assert point((cx, cy), int(r) + 1, (px, py))
    assert not point((cx, cy), int(r - 0.001), (px, py))
