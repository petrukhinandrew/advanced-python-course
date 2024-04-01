from time import sleep
from sys import stdin, stdout
from select import select
from codecs import encode
from multiprocessing import Pipe, Queue, Process
from logging import basicConfig, INFO, info
from time import time

def target_A(inp, outq: Queue):
    while True:
        in_data = inp.recv()
        res = in_data.lower()
        outq.put(res)
        sleep(5)


def target_B(inq, outp):
    while True:
        in_data = inq.get()
        res = encode(in_data, 'rot13')
        outp.send(res)


if __name__ == "__main__":
    basicConfig(filename="artifacts/task3.txt", filemode='w', level=INFO, format='%(asctime)s - %(message)s')

    stdin_pipe = Pipe()
    stdout_pipe = Pipe()
    
    q = Queue()
    A = Process(target=target_A, args=(stdin_pipe[0], q))
    B = Process(target=target_B, args=(q, stdout_pipe[1]))
    A.start()
    B.start()
    info("Process's started")
    while True:
        read_list, _, _ = select([stdin.fileno(), stdout_pipe[0]], [], [])
        quit = False
        for src in read_list:
            if src == stdin.fileno():
                info("select stdin at " + str(time()))
                buf = stdin.readline().strip(" \n")
                info("stdin got " + buf)
                if buf == "quit":
                    quit = True
                    break
                stdin_pipe[1].send(buf)
            elif src == stdout_pipe[0]:
                info("select out pipe at " + str(time()))
                out_data = stdout_pipe[0].recv()
                info("out pipe got " + out_data)
                stdout.write(out_data + "\n")
                stdout.flush()
                info("wrote out pipe data to stdout at " + str(time())) 
        if quit:
            break
    A.terminate()
    B.terminate()
    
