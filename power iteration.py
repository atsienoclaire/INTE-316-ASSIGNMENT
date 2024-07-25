import numpy as np

def power_iteration(A, num_simulations):
    b_k = np.random.rand(A.shape[1])
    
    for _ in range(num_simulations):
        # Calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)
        
        # Calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)
        
        # Re-normalize the vector
        b_k = b_k1 / b_k1_norm
    
    eigenvalue = np.dot(np.dot(A, b_k), b_k) / np.dot(b_k, b_k)
    return eigenvalue, b_k

# Given matrix
A = np.array([
    [4, 1, 1],
    [1, 3, -1],
    [1, -1, 2]
])

# Compute the dominant eigenvalue and eigenvector
eigenvalue, eigenvector = power_iteration(A, 100)
print("Dominant Eigenvalue (Power Iteration):", eigenvalue)
print("Corresponding Eigenvector (Power Iteration):", eigenvector)
