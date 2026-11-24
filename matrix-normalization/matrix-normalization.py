import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    m = np.asarray(matrix,dtype=float)
    row , column = m.shape
    if norm_type == "l1":
        if axis == 1 :
            sum = np.zeros(row)
            for i in range(row):
                for j in range(column):
                    sum[i] += m[i,j]
                for j in range(column):
                    if sum[i] != 0.0:
                        m[i,j] = m[i,j] / sum[i]
                    else :
                        m[i,j] = 0.0
        elif axis == 0:
            sum = np.zeros(column)
            for j in range(column):
                for i in range(row):
                    sum[j] += m[i,j]
                for i in range(row):
                    if sum[j] != 0.0:
                        m[i,j] = m[i,j] / sum[j]
                    else :
                            m[i,j] = 0.0
        else:
            sum = 0.0
            for j in range(column):
                for i in range(row):
                    sum+= m[i,j]
            for i in range(row):
                for j in range(column):
                    if sum  !=0.0:
                        m[i,j] = m[i,j] / sum
                    else :
                        m[i,j] = 0.0                    
    elif norm_type == "l2":
        if axis == 1 :
            sum = np.zeros(row)
            for i in range(row):
                for j in range(column):
                    sum[i] += m[i,j]**2
            for i in range(row):
                sum [i] = np.sqrt(sum[i])
                for j in range(column):
                    if sum[i] !=0.0:
                        m[i,j] = m[i,j] / sum[i]
                    else :
                        m[i,j] = 0.0
        elif axis == 0:
            sum = np.zeros(column)
            for j in range(column):
                for i in range(row):
                    sum[j] += m[i,j]**2
            for j in range(column):
                sum [j] = np.sqrt(sum[j])
                for i in range(row):
                    if sum[j] !=  0.0:
                        m[i,j] = m[i,j] / sum[j]     
                    else :
                        m[i,j] = 0.0
        else :
            sum = 0.0
            for j in range(column):
                for i in range(row):
                    sum+= m[i,j]**2
            sum = np.sqrt(sum)
            for i in range(row):
                for j in range(column):
                    if sum != 0.0:
                        m[i,j] = m[i,j] / sum
                    else :
                        m[i,j] = 0.0
    else:
        if axis == 1 :
            sum = np.zeros(row)
            for i in range(row):
                for j in range(column):
                    if(sum[i] < m[i,j]):
                        sum[i] = m[i,j]
            for i in range(row):
                
                for j in range(column):
                    if sum[i] != 0.0:
                        m[i,j] = m[i,j] / sum[i]
                    else :
                        m[i,j] = 0.0
        elif axis == 0:
            sum = np.zeros(column)
            for j in range(column):
                for i in range(row):
                    if(sum[j] < m[i,j]):
                        sum[j] = m[i,j]
            for j in range(column):
                
                for i in range(row):
                    if sum[j] != 0.0:
                        m[i,j] = m[i,j] / sum[j] 
                    else :
                        m[i,j] = 0.0
        else :
            sum = 0.0
            for j in range(column):
                for i in range(row):
                    if(sum < m[i,j]):
                        sum = m[i,j]
            
            for i in range(row):
                for j in range(column):
                    if sum !=  0.0:
                        m[i,j] = m[i,j] / sum   
                    else :
                        m[i,j] = 0.0
    return m