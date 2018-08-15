# 子进程 并不是自身而是一个外部进程 创建之后还要控制输入和输出

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('结束代码：', r)
