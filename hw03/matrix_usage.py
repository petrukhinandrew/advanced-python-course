import numpy as np
from base_matrix import BaseMatrix
from matrix_mixin import MixedMatrix
from cached_matrix import HashableMatrix

ARTIFACTS_PATH = "./artifacts/"


def setup_np():
    np.random.seed(0)


def task1_sol():
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
    A = MixedMatrix(np.random.randint(0, 10, (10, 10)).tolist())
    B = MixedMatrix(np.random.randint(0, 10, (10, 10)).tolist())
    A.save_as(ARTIFACTS_PATH + "2/A.txt")
    B.save_as(ARTIFACTS_PATH + "2/B.txt")
    res = A + B
    res.save_as(ARTIFACTS_PATH + "2/matrix+.txt")
    res = A * B
    res.save_as(ARTIFACTS_PATH + "2/matrix*.txt")
    res = A @ B
    res.save_as(ARTIFACTS_PATH + "2/matrix@.txt")


def task3_sol():
    A = HashableMatrix([[1, 1], [3, 4]])
    B = HashableMatrix([[1, 2], [2, 1]])
    C = HashableMatrix([[0, 0], [3, 4]])
    D = HashableMatrix([[1, 2], [2, 1]])

    # assert hash(A) == hash(C)
    assert A != C
    assert B == D

    with open(ARTIFACTS_PATH + "3/A.txt", 'w') as aF:
        aF.write(str(A))
    with open(ARTIFACTS_PATH + "3/B.txt", 'w') as bF:
        bF.write(str(B))
    with open(ARTIFACTS_PATH + "3/C.txt", 'w') as cF:
        cF.write(str(A))
    with open(ARTIFACTS_PATH + "3/D.txt", 'w') as dF:
        dF.write(str(A))

    with open(ARTIFACTS_PATH + "3/AB.txt", 'w') as abF:
        abF.write(str(A @ B))
    
    HashableMatrix._cache = {} # want proper C @ D value in artifacts
    
    with open(ARTIFACTS_PATH + "3/CD.txt", 'w') as cdF:
        cdF.write(str(C @ D))
    with open(ARTIFACTS_PATH + "3/hash.txt", 'w') as hF:
        hF.write(str(hash(A @ B)))


if __name__ == "__main__":
    setup_np()
    task1_sol()
    task2_sol()
    task3_sol()
