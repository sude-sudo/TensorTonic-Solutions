import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    m = np.asarray(matrix,dtype = float)
    if norm_type == "l1":
        norms =  np.sum(np.abs(m),axis = axis,keepdims=True)
    elif norm_type =="l2":
        norms =  np.sqrt(np.sum(m**2,axis = axis,keepdims = True))
    else:
        norms =  np.max(np.abs(m),axis,keepdims = True)
    safe_norms = np.where(norms == 0,1.0,norms)
    return m / safe_norms
