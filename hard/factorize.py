import random

from pytest import mark


def factorize(n):
    """
    Дано натуральное число n
    Разложить его на простые делители и вернуть пары вида (простое, степень вхождения)
    в порядке возрастания

    factorize(84) :returns [(2, 2), (3, 1), (7, 1)] # т.к. 84 = 2^2 * 3 * 7
    """
    pass


@mark.parametrize('data', [
    [1, []],
    [2, [(2, 1)]],
    [3, [(3, 1)]],
    [84, [(2, 2), (3, 1), (7, 1)]],
    [1024, [(2, 10)]],
    [73 * 73, [(73, 2)]],
    [5 * 5 * 5 * 239, [(5, 3), (239, 1)]]
])
def test_factorize(data):
    assert factorize(data[0]) == data[1]


@mark.parametrize('seed', list(range(50)))
def test_randomized(seed):
    random.seed(seed)
    primes = [2, 3, 13, 17, 37, 173, 977]
    n, ans = 1, {}
    while n < 7000:
        p = random.choice(primes)
        if seed >= 20:
            p = min(p, random.choice(primes))
        ans[p] = ans.get(p, 0) + 1
        n *= p
    ans = sorted(ans.items())
    print(ans)
    assert factorize(n) == ans
