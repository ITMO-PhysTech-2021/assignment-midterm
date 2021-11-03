import random

from pytest import mark


def url(s):
    """
    Дана строка s, описывающая адрес страницы в интернете, в формате схема://адрес.сайта/путь
    Вернуть кортеж из трех строк: (схема, адрес.сайти, путь)

    url('https://codeforces.com/contests/1607') :returns ('https', 'codeforces.com', 'contests/1607')
    """
    pass


# noinspection HttpUrlsUsage
@mark.parametrize('data', [
    ['https://cf.ru/xyz', ('https', 'cf.ru', 'xyz')],
    ['http://cf.ru/xyz', ('http', 'cf.ru', 'xyz')],
    ['ftp://domain.me.to/', ('ftp', 'domain.me.to', '')],
    ['C://dir/file', ('C', 'dir', 'file')],  # Странный пример, так и задумано, не вникайте
    ['https://cf.ru/x/y/z', ('https', 'cf.ru', 'x/y/z')],
    ['hs://x.y.z.t/t/z/y/x', ('hs', 'x.y.z.t', 't/z/y/x')],
])
def test_url(data):
    assert url(data[0]) == data[1]


@mark.parametrize('seed', list(range(20)))
def test_randomized(seed):
    random.seed(seed)

    def __word(n):
        return ''.join([chr(random.randint(ord('a'), ord('z'))) for _ in range(n)])

    scheme = __word(7)
    domain = '.'.join([__word(i) for i in range(1, 7)])
    path = '/'.join([__word(i % 3) for i in range(6)])
    assert url(f'{scheme}://{domain}/{path}') == (scheme, domain, path)