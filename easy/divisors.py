import random

from pytest import mark


def divisors(n):
    """
    Дано натуральное число n
    Вернуть массив из всех его натуральных делителей в порядке возрастания

    divisors(12) :returns [1, 2, 3, 4, 6, 12]
    """
    pass


@mark.parametrize('data', [
    [1, [1]],
    [2, [1, 2]],
    [3, [1, 3]],
    [12, [1, 2, 3, 4, 6, 12]],
    [1024, [2 ** i for i in range(11)]],
    [73 * 73, [1, 73, 73 * 73]],
    [5 * 5 * 239, [1, 5, 25, 239, 239 * 5, 239 * 25]]
])
def test_divisors(data):
    assert divisors(data[0]) == data[1]


@mark.parametrize('seed', list(range(20)))
def test_randomized(seed):
    random.seed(seed)
    primes = [2, 3, 13, 17, 37, 173, 977]
    n, ans = 1, {1}
    while n < 1000:
        p = random.choice(primes)
        n *= p
        ans = ans.union([d * p for d in ans])
    assert divisors(n) == sorted(list(ans))
