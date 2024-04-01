from time import perf_counter


def fib(n: int):
    return fib(n - 1) + fib(n - 2) if n > 1 else n


def sync_fib(n: int, iters: int) -> float:
    st = perf_counter()

    for _ in range(iters):
        fib(n)

    return perf_counter() - st


def threading_fib(n: int, iters: int) -> float:
    import threading
    threads = [threading.Thread(target=fib, args=(n, )) for _ in range(iters)]

    st = perf_counter()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return perf_counter() - st


def multiproc_fib(n: int, iters: int) -> float:
    import multiprocessing
    procs = [multiprocessing.Process(target=fib, args=(n, ))
             for _ in range(iters)]

    st = perf_counter()

    for p in procs:
        p.start()

    for p in procs:
        p.join()

    return perf_counter() - st


if __name__ == "__main__":
    sync_time = sync_fib(36, 10)
    thread_time = threading_fib(36, 10)
    proc_time = multiproc_fib(36, 10)
    with open("artifacts/task1.txt", 'w') as artifact:
        artifact.write("sync: {}\n".format(sync_time))
        artifact.write("threading: {}\n".format(thread_time))
        artifact.write("multiprocessing: {}\n".format(proc_time))
