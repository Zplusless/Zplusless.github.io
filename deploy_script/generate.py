import os

lines = [
    '# Mindmap list\n'
]

print('generating TOC')

for file in os.listdir('.'):
    if 'html' in file:
        lines.append('[{}]({})'.format(file,'https://Zplusless.github.io/'+file)+'\n\n')

with open('./README.MD', 'w') as readme:
    readme.writelines(lines)


print('done!')