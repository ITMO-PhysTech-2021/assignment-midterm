import random
from functools import reduce

from pytest import mark


def bind(f, **kwargs):
    """
    Дана функция f от нескольких аргументов и ОДИН аргумент вида _number=value, например _1='x' или _5=122
    Такой аргумент означает, что надо подставить value в f в качестве аргумента номер number
    Вернуть функцию, принимающую на один аргумент меньше аргументов, делающую эту подстановку

    bind(lambda x, y: x - y, _1=10)             :returns lambda y: 10 - y
    bind(lambda x, y: x - y, _2=10)             :returns lambda x: x - 10
    bind(lambda x, y, z: x + y + z, _2='++')    :returns lambda x, z: x + '++' + z
    """
    pass


def test_example():
    for x, y in [(1, 2), (2, 1), (0, 3), (4, 0)]:
        assert bind(lambda x, y: x - y, _1=x)(y) == x - y
        assert bind(lambda x, y: x - y, _2=y)(x) == x - y
    for x, z in [('12', ''), ('', '()'), ('-', '++')]:
        assert bind(lambda x, y, z: x + y + z, _2='++')(x, z) == x + '++' + z


@mark.parametrize('seed', list(range(5)))
def test_0_arguments(seed):
    random.seed(seed)
    res = random.randint(1, 1000)
    assert bind(lambda x: res, _1=0)() == res
    assert bind(lambda x: res, _1=random.randint(1, 1000))() == res
    for t in range(10):
        assert bind(lambda x: x + res, _1=t)() == t + res


@mark.parametrize('n', list(range(1, 8)))
def test_sum(n):
    random.seed(n)
    f = lambda *args: sum(args) if len(args) == n else None
    data = [random.randint(1, 1000) for _ in range(n)]
    res = random.randint(1, 1000)
    assert bind(lambda *args: sum(args), _1=res)(*data) == res + sum(data)
    assert bind(f, _1=res)(*data) is None
    assert bind(lambda *args: sum(args), **{f'_{n+1}': res})(*data) == res + sum(data)
    assert bind(f, **{f'_{n+1}': res})(*data) is None


def test_last():
    random.seed(0)
    data = [random.randint(1, 1000) for _ in range(10)]
    d = -random.randint(1, 1000)
    f = lambda *args: args[0] + args[-1]
    assert bind(f, _1=d)(*data) == d + data[-1]
    assert bind(f, _2=d)(*data) == data[0] + data[-1]
    assert bind(f, _10=d)(*data) == data[0] + data[-1]
    assert bind(f, _11=d)(*data) == data[0] + d