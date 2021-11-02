import random

from pytest import mark


def rfloor(n, d):
    """
    Даны два вещественных числа n и d, при чем d - положительное
    "Округлить" n до ближайшего снизу числа, представимого как d * k, где k - целое

    rfloor(2.3, 0.7) :returns 2.1  (= 0.7 * 3)
    """
    pass


@mark.parametrize('data', [
    [2.2, 0.3, 2.1],
    [2.2, 0.4, 2.0],
    [0.0, 123.32, 0.0],
    [123.32, 123.32, 123.32],
    [123.32, 123.321, 0.0],
    [-2.5, 0.5, -2.5],
    [-2.5, 0.6, -3.0]
])
def test_unround(data):
    assert rfloor(data[0], data[1]) == data[2]


@mark.parametrize('seed', list(range(20)))
def test_randomized(seed):
    random.seed(seed)
    n = random.uniform(-1000.0, 1000.0)
    d = random.uniform(0.0001, 1000.0) ** 0.5
    res = rfloor(n, d)
    assert abs(res / d - int(res / d)) < 0.00001
    assert res <= n
    assert res + d > n
