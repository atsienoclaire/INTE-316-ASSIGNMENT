import numpy as np

def qr_algorithm(A, num_iterations):
    n = A.shape[0]
    Q_total = np.eye(n)
    
    for _ in range(num_iterations):
        Q, R = np.linalg.qr(A)
        A = np.dot(R, Q)
        Q_total = np.dot(Q_total, Q)
    
    eigenvalues = np.diag(A)
    eigenvectors = Q_total
    return eigenvalues, eigenvectors

# Define the matrix A
A = np.array([
    [4, 1, 1],
    [1, 3, -1],
    [1, -1, 2]
])

# Compute eigenvalues and eigenvectors using QR Algorithm
eigenvalues_qr, eigenvectors_qr = qr_algorithm(A, 100)
print("Eigenvalues (QR Algorithm):", eigenvalues_qr)
print("Eigenvectors (QR Algorithm):", eigenvectors_qr)
