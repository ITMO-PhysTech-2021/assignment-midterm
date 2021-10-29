import random

from pytest import mark


def revwords(s):
    """
    Дана строка s, состоящая из "слов", разделенных пробелами
    Вернуть строку, в которой все те же слова идут в обратном порядке

    revwords('good morning world') :returns 'world morning good'
    """
    pass


@mark.parametrize('data', [
    ['', ''],
    ['x y', 'y x'],
    ['one', 'one'],
    ['one two three', 'three two one'],
    ['same same same', 'same same same'],
    ['word & another word', 'word another & word'],
    ['word & anotherword', 'anotherword & word'],
    ['word&another-word', 'word&another-word']
])
def test_revwords(data):
    assert revwords(data[0]) == data[1]
