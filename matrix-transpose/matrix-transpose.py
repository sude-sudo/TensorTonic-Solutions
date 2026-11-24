import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A = np.asarray(A,dtype = float)
    shape = np.shape(A)
    B = np.zeros(shape[::-1],dtype=float)
    m,n = A.shape
    for i in range(m):
        for j in range(n):
            B[j,i] = A[i,j]
    return B

