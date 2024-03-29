from matrix_impl import BaseMatrix
ARTIFACTS_PATH = "./artifacts/"

def task1_sol():
    import numpy as np
    np.random.seed(0)

    A = BaseMatrix(np.random.randint(0, 10, (10, 10)).tolist())
    B = BaseMatrix(np.random.randint(0, 10, (10, 10)).tolist())
    
    with open(ARTIFACTS_PATH + "1/matrix+.txt", "w") as outp:
        res = A + B
        outp.write(str(A) + "\n")
        outp.write("+\n")
        outp.write(str(B) + "\n")
        outp.write("=\n")
        outp.write(str(res))
    
    with open(ARTIFACTS_PATH + "1/matrix*.txt", "w") as outp:
        res = A * B
        outp.write(str(A) + "\n")
        outp.write("*\n")
        outp.write(str(B) + "\n")
        outp.write("=\n")
        outp.write(str(res))
    
    with open(ARTIFACTS_PATH + "1/matrix@.txt", "w") as outp:
        res = A @ B
        outp.write(str(A) + "\n")
        outp.write("@\n")
        outp.write(str(B) + "\n")
        outp.write("=\n")
        outp.write(str(res))
    
def task2_sol():
    pass
def task3_sol():
    pass


if __name__ == "__main__":
    task1_sol()
    task2_sol()
    task3_sol()