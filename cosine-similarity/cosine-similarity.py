import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    
    x = np.asarray(a,dtype = float)
    y = np.asarray(b,dtype = float)
    z = float(np.dot(x,y))
    if(np.linalg.norm(x) * np.linalg.norm(y) != 0.0):
        return z / float((np.linalg.norm(x) * np.linalg.norm(y) ))
    else:
        return 0.0