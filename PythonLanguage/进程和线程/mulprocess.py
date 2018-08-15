# 跨平台多进程支持

from multiprocessing import Process
import os

# 子进程执行的代码
def run_proc(name):
    print('运行子进程 %s %s' % (name, os.getpid()))

if __name__ == '__main__':
    print('父进程 %s' % os.getpid())
    # 创建一个进程对象，传递进来进程的执行方法和进程需要的元组参数
    p = Process(target=run_proc, args=('test',))
    print('子进程将要开始')
    p.start()
    # 方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    print('子进程结束')
