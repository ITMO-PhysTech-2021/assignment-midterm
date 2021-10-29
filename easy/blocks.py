import random

from pytest import mark


def blocks(a, k):
    """
    Дан массив a и натуральное число k
    Вернуть массив из "блоков" из подряд идущих элементов a длины k
    Если длина массива не делится на k, последний блок будет неполным

    blocks([1, 2, 3, 4, 5, 6, 7], 3) :returns [[1, 2, 3], [4, 5, 6], [7]]
    """
    pass


@mark.parametrize('data', [
    [[], 1, []],
    [[], 2, []],
    [[1], 1, [[1]]],
    [[1], 2, [[1]]],
    [[3, 1], 1, [[3], [1]]],
    [[3, 1], 3, [[3, 1]]],
    [[1, 5, 3, 2, 6], 2, [[1, 5], [3, 2], [6]]]
])
def test_blocks(data):
    assert blocks(data[0], data[1]) == data[2]


@mark.parametrize('seed', list(range(20)))
def test_randomized(seed):
    random.seed(seed)
    k = random.randint(1, 10)
    blk, ans = [], []
    for b in range(random.randint(7, 13)):
        blk.append([random.randint(1, 1000) for _ in range(k)])
        ans += blk[-1]
    if random.randint(0, 1) and k > 1:
        blk[-1] = blk[-1][:-1]
        ans.pop()
    assert blocks(ans, k) == blk
