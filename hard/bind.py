import random
from functools import reduce

from pytest import mark


def bind(f, n, **kwargs):
    """
    Дана функция f от n аргументов
    Каждый из kwargs имеет вид _number=value, например _1='x' или _5=122
    Вернуть функцию f, в которую уже подставлены значения для аргументов, переданные в kwargs

    liftmap(lambda x, y: x ** y, lambda a: 2 * a) :returns lambda x, y: (2 * x) ** (2 * y)
    liftmap(lambda x, y: x + y, lambda a: 2)      :returns lambda x, y: 2 + 2
    """
    pass


def test_example():
    for x, y in [(1, 2), (2, 1), (0, 3), (4, 0)]:
        assert liftmap(lambda x, y: x ** y, lambda a: 2 * a)(x, y) == (2 * x) ** (2 * y)
        assert liftmap(lambda x, y: x + y, lambda a: 2)(x, y) == 4


@mark.parametrize('seed', list(range(5)))
def test_0_arguments(seed):
    random.seed(seed)
    res = random.randint(1, 1000)
    f = lambda: res
    for g in [lambda _: 1, lambda a: a, lambda: None]:
        assert liftmap(f, g)() == res


@mark.parametrize('n', list(range(1, 8)))
def test_sum(n):
    f = lambda *args: sum(args) if len(args) == n else None
    data = [random.randint(1, 1000) for _ in range(n)]
    assert liftmap(f, lambda a: a)(*data) == sum(data)
    assert liftmap(f, lambda a: 1)(*data) == n
    assert liftmap(f, lambda a: a * 2)(*data) == 2 * sum(data)
    assert liftmap(f, lambda a: a if a % 3 == 0 else 0)(*data) == sum(filter(lambda a: a % 3 == 0, data))