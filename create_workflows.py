import os

for file in os.listdir('.github/workflows'):
    os.remove(f'.github/workflows/{file}')

template = ''.join(open('.github/.yaml.tmp').readlines())
root_blacklist = ['.py', '.md', '.gitignore']

for root in os.listdir('.'):
    if root.startswith('.'):
        continue
    if any([root.endswith(ext) for ext in root_blacklist]):
        continue
    for task in os.listdir(root):
        if not task.endswith('.py'):
            continue
        _path = f'{root}/{task}'
        _name = task[:-3]

        config = template.format(
            _full_name=f'{_name} [{root}]',
            _name=_name,
            _path=_path,
        )
        with open(f'.github/workflows/{_name}.yaml', 'w') as wf:
            print(config.rstrip(), file=wf)
