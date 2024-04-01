import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from concurrent.futures._base import Executor
from multiprocessing import cpu_count
from logging import basicConfig, INFO, info

def integrate(f, a, b, *, n_jobs=1, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def subint(f, l, r, step):
    acc = 0
    i = l
    while i < r:
        acc += f(i) * min(step, r - i)
        i += step
    return acc


def int_executors(exec_instance: Executor, f, a, b, *, n_jobs=1, n_iter=10000000):
    res = 0
    segment_step = (b - a) / n_jobs
    int_step = (b - a) / n_iter
    with exec_instance(max_workers=n_jobs) as executor:
        futures = [executor.submit(subint, f, a + (i * segment_step),
                                   a + ((i + 1) * segment_step), int_step) for i in range(n_jobs)]
        res = sum(map(lambda x: x.result(), futures))
    return res


def int_tps(f, a, b, *, n_jobs=1, n_iter=10000000):
    return int_executors(ThreadPoolExecutor, f, a, b, n_jobs=n_jobs, n_iter=n_iter)


def int_pps(f, a, b, *, n_jobs=1, n_iter=10000000):
    return int_executors(ProcessPoolExecutor, f, a, b, n_jobs=n_jobs, n_iter=n_iter)


def calc_exec_time():
    pass

if __name__ == "__main__":
    basicConfig(filename="artifacts/task2.txt", filemode='w', level=INFO, format='%(asctime)s - %(message)s')
    int_args = (math.cos, 0, math.pi / 2)
    info("ThreadPoolExecutor")
    for n in range(1, cpu_count() * 2):
        info("n_jobs={}: {}".format(n, int_tps(*int_args, n_jobs=n)))
    info("==================")
    info("ProcessPoolExecutor")
    for n in range(1, cpu_count() * 2):
        info("n_jobs={}: {}".format(n, int_pps(*int_args, n_jobs=n)))
    info("==================")
