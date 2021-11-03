import base64
import os
import random
import sys
import traceback

from prepare import list_tasks

'''
Не редактируйте этот файл!
Запустите его ОДИН раз в самом начале, чтобы сгенерировать свой вариант.
'''

name = os.path.dirname(os.getcwd())
random.seed(name)
_points = {
    'easy': 2,
    'hard': 5
}


def pick(root, tasks, cnt, out=sys.stdout):
    random.shuffle(tasks)
    pts = _points[root]
    variant = tasks[:cnt]
    print(f'Вариант [{root}]:', file=out)
    for task in variant:
        print(f' - {task} - {pts} pts', file=out)
    print(f'Все остальные задачи из \'{root}\' стоят {pts / 2} pts\n', file=out)


def _precalc(limit):
    limit += 1
    c = [[0 for _1 in range(limit)] for _2 in range(limit)]
    c[0][0] = 1
    for i in range(1, limit):
        c[i][0] = 1
        for j in range(1, len(c[i])):
            c[i][j] = c[i - 1][j] + c[i - 1][j - 1]

    return lambda n, k: c[n][k]


if __name__ == '__main__':
    tasks = list_tasks()
    c = _precalc(max(map(len, tasks.values())))

    if os.path.exists(f'{os.curdir}/.variant'):
        if input('Вариант уже сгенерирован, сгенерировать заново? [y/n]\n') != 'y':
            exit(0)
        else:
            os.remove('.variant')

    with open('.variant', 'w', encoding='utf-8') as var:
        try:
            for root in ['easy', 'hard']:
                n = len(tasks[root])
                sel = n // 2
                while c(n, sel - 1) > 100 and _points[root] * (sel - 1) >= 6:
                    sel -= 1
                pick(root, tasks[root], sel, out=var)

            with open('.github/.secret', 'r') as gl:
                data = gl.read()
                lines = base64.b64decode(data).decode('utf-8').split('\n')
                for line in lines:
                    print(line.rstrip(), file=var)
        except (BaseException, Exception) as e:
            var.close()
            os.remove('.variant')
            print('Что-то пошло не так, напишите об этом преподавателю:')
            traceback.print_exc()
            exit(0)

    print('Вариант успешно сгенерирован в файл .variant в корне проекта')
