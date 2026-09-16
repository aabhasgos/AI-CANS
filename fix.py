import os
import glob
for f in glob.glob('backend/api/*.py'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if '\\"\\"\\"' in content:
        print(f'Fixing {f}')
        content = content.replace('\\"\\"\\"', '"""')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
