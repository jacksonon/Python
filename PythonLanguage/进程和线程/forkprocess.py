import os

print('Process （%s）开始...' % os.getpid())

# 轻松创建子进程
pid = os.fork()
if pid == 0:
    print('子进程%s 父进程%s' % (os.getpid(), os.getppid()))
else:
    print('%s 创建了一个子进程 %s' % (os.getpid(), pid))


