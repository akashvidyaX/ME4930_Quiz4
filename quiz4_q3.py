import sympy as sp
import numpy as np

# Define the symbolic angles alpha, beta, and gamma
alpha, beta, gamma = sp.symbols('alpha beta gamma')

# Define the basic rotation matrices Rz and Rx
Rz_alpha = sp.Matrix([[sp.cos(alpha), -sp.sin(alpha), 0],
                      [sp.sin(alpha), sp.cos(alpha), 0],
                      [0, 0, 1]])

Rx_beta = sp.Matrix([[1, 0, 0],
                     [0, sp.cos(beta), -sp.sin(beta)],
                     [0, sp.sin(beta), sp.cos(beta)]])

Rz_gamma = sp.Matrix([[sp.cos(gamma), -sp.sin(gamma), 0],
                      [sp.sin(gamma), sp.cos(gamma), 0],
                      [0, 0, 1]])

# Compute the product of the rotation matrices to obtain the ZXZ Euler angles rotation matrix
R_zxz = Rz_alpha * Rx_beta * Rz_gamma
R_zxz.simplify()
print(R_zxz)


# Given rotation matrix from Question 3
R_q3 = np.array([[-1/np.sqrt(2), 1/np.sqrt(2), 0],
                 [-0.5, -0.5, 1/np.sqrt(2)],
                 [0.5, 0.5, 1/np.sqrt(2)]])

# Verify the orthogonality property R * R.T = I
orthogonality_check = np.allclose(np.dot(R_q3, R_q3.T), np.eye(3))

# Verify the determinant property det(R) = 1
determinant_check = np.isclose(np.linalg.det(R_q3), 1)

# Checking both properties
print(orthogonality_check)
print(determinant_check)
