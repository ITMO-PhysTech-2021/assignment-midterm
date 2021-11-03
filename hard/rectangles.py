import random

from pytest import mark


def rectangles(pts):
    """
    Дан непустой массив pts четверок чисел, в каждой четверке - (x1, y1, x2, y2) -
    координаты противоположных углов одного прямоугольника
    Вернуть площадь пересечения всех этих прямоугольников

    rectangles([(0, 0, 3, 3), (4, 5, 2, 1)]) :returns 2
    """
    return


@mark.parametrize('data', [
    [[(0, 0, 3, 3), (4, 5, 2, 1)], 2],
    [[(1, 4, 4, 1), (0, 2, 10, 9)], 6],
    [[(4, 5, 2, 9)], 8],
    [[(0, 0, 7, 2), (7, 6, 1, 2)], 0],
    [[(0, 0, 1, 1), (1, 1, 2, 2)], 0],
    [[(7, 6, 12, 1), (9, 3, 8, 1)], 2],
    [[(0, 10, 11, 2), (20, 3, 6, 12), (1, 4, 17, 6), (14, 7, 3, 0), (10, 1, 8, 14)], 4],
])
def test_rectangles(data):
    assert rectangles(data[0]) == data[1]


def _common(size, x1, x2, y1, y2):
    pts = []
    for i in range(size):
        b = [random.randint(-1000, x1), random.randint(-1000, y1),
             random.randint(x2, 1000), random.randint(y2, 1000)]
        pts.append(b)
    pts[random.randint(0, size - 1)][0] = x1
    pts[random.randint(0, size - 1)][2] = x2
    pts[random.randint(0, size - 1)][1] = y1
    pts[random.randint(0, size - 1)][3] = y2
    for b in pts:
        if random.randint(0, 1) == 0:
            b[0], b[2] = b[2], b[0]
        if random.randint(0, 1) == 0:
            b[1], b[3] = b[3], b[1]
    random.shuffle(pts)
    return pts


@mark.parametrize('seed', list(range(1, 11)))
def test_empty(seed):
    random.seed(seed)
    x = random.randint(-1000, 1000)
    y = random.randint(-1000, 1000)
    pts = _common(seed, x, x, y, y)
    assert rectangles(pts) == 0


@mark.parametrize('seed', list(range(1, 20)))
def test_randomized(seed):
    random.seed(seed)
    x1, x2 = random.randint(-1000, -1), random.randint(1, 1000)
    y1, y2 = random.randint(-1000, -1), random.randint(1, 1000)
    pts = _common(seed, x1, x2, y1, y2)
    assert rectangles(pts) == (y2 - y1) * (x2 - x1)
