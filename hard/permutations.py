import random

from pytest import mark


def permutations(n):
    """
    Дано целое неотрицательное число n
    Вернуть массив из всех перестановок чисел от 1 до n в алфавитном порядке (см. примеры)

    permutations(2) :returns [
        [1, 2],
        [2, 1]
    ]
    permutations(3) :returns [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]
    """
    pass


@mark.parametrize('data', [
    [0, [[]]],
    [1, [[1]]],
    [2, [[1, 2], [2, 1]]],
    [3, [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]]
])
def test_permutations(data):
    assert permutations(data[0]) == data[1]


@mark.parametrize('n', list(range(4, 10)))
def test_large(n):
    res = permutations(n)
    expected_len = 1
    for i in range(2, n + 1):
        expected_len *= i
    assert len(res) == expected_len
    for item in res:
        assert set(item) == set(range(1, n + 1))
    for i in range(1, len(res)):
        assert res[i - 1] < res[i]
