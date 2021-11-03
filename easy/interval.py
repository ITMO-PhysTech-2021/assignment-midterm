import random

from pytest import mark


def interval(t1, t2):
    """
    Даны два момента времени в формате пар (часы, минуты)
    Вернуть время, прошедшее между двумя ближайшими моментами, когда на часах были
    состояния t1 и t2, в таком же формате (пара из часов и минут)

    interval((23, 51), (2, 17)) :returns (2, 26)
    """
    pass


@mark.parametrize('data', [
    [(1, 10), (1, 19), (0, 9)],
    [(1, 0), (1, 59), (0, 59)],
    [(1, 4), (3, 59), (2, 55)],
    [(1, 59), (1, 0), (23, 1)],
    [(0, 14), (23, 11), (22, 57)],
    [(10, 9), (9, 10), (23, 1)],
    [(3, 10), (17, 1), (13, 51)],
    [(3, 27), (3, 27), (0, 0)]
])
def test_interval(data):
    assert interval(data[0], data[1]) == data[2]


@mark.parametrize('seed', list(range(20)))
def test_randomized(seed):
    random.seed(seed)
    t1 = (random.randint(0, 23), random.randint(0, 60))
    t2 = (random.randint(0, 23), random.randint(0, 60))
    i1, i2 = interval(t1, t2), interval(t2, t1)
    assert i1[0] < 24 and i2[0] < 24
    assert i1[1] < 60 and i2[1] < 60
    assert i1[1] + i2[1] in [0, 60]
    assert i1[0] + i2[0] + int(i1[1] + i2[1] > 0) == 24
