import os


def clear():
    for file in os.listdir('.github/workflows'):
        os.remove(f'.github/workflows/{file}')


def list_tasks():
    root_blacklist = ['.py', '.md', '.gitignore']
    tasks = {}

    for root in os.listdir('.'):
        if root.startswith('.'):
            continue
        if any([root.endswith(ext) for ext in root_blacklist]):
            continue
        tasks[root] = []
        for task in os.listdir(root):
            if not task.endswith('.py'):
                continue
            name = task[:-3]
            tasks[root].append(name)

    for _, block in tasks.items():
        block.sort()
    return tasks


if __name__ == '__main__':
    clear()

    template = ''.join(open('.github/.yaml.tmp').readlines())
    tasks = list_tasks()

    for root, block in tasks.items():
        for name in block:
            config = template.format(
                _full_name=f'Task {name} [{root}]',
                _name=name,
                _path=f'{root}/{name}.py',
            )
            with open(f'.github/workflows/{name}.yaml', 'w') as wf:
                print(config.rstrip(), file=wf)
