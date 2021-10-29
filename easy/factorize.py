import random

from pytest import mark


def factorize(n):
    """
    Разложить число n на простые делители и вернуть их в порядке возрастания
    factorize(84) :returns [2, 2, 3, 7]
    """
    pass


@mark.parametrize('data', [
    [1, []],
    [2, [2]],
    [3, [3]],
    [84, [2, 2, 3, 7]],
    [1024, [2] * 10],
    [73 * 73, [73, 73]],
    [5 * 5 * 5 * 239, [5, 5, 5, 239]]
])
def test_factorize(data):
    assert factorize(data[0]) == data[1]


@mark.parametrize('seed', range(20))
def test_randomized(seed):
    random.seed(seed)
    primes = [2, 3, 13, 17, 37, 173, 977]
    n, ans = 1, []
    while n < 1000:
        ans.append(random.choice(primes))
        n *= ans[-1]
    ans.sort()
    assert factorize(n) == ans
