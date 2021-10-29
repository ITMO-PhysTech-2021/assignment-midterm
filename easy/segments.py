import random

from pytest import mark


def segments(points):
    """
    Дан массив различных целых чисел points (массив четной длины)
    Объединить числа в пары соседних в порядке возрастания

    segments([1, 8, 5, 2, 11, 7]) :returns [(1, 2), (5, 7), (8, 11)]
    """
    pass


@mark.parametrize('data', [
    [[], []],
    [[2, 1], [(1, 2)]],
    [[4, 2, 1, 3], [(1, 2), (3, 4)]],
    [[1, 7, 33, -100], [(-100, 1), (7, 33)]],
    [[1, 2 ** 32], [(1, 2 ** 32)]],
    [[1, 8, 5, 2, 11, 7], [(1, 2), (5, 7), (8, 11)]]
])
def test_segments(data):
    assert segments(data[0]) == data[1]


@mark.parametrize('seed', range(20))
def test_randomized(seed):
    random.seed(seed)
    a = list(range(1000))
    random.shuffle(a)
    a = a[:500]
    res = segments(a[:])
    items = [item for pair in res for item in pair]
    assert set(a) == set(items)
    for i in range(1, len(items)):
        assert items[i - 1] < items[i]
