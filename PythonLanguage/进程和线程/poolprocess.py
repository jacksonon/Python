# 启动大量的子进程 进程池批量创建

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('运行任务 %s  %s' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('任务 %s 运行了 %.2f 秒' % (name, (end- start)))

if __name__ == '__main__':
    print('父进程 %s' % os.getpid())
    # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    # 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i, ))
    print('等待所有子进程创建结束...')
    p.close()
    p.join()
    print('所有子进程结束')