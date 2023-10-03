from sympy import Matrix, symbols, sin, cos, sqrt

# Define vectors w1 and w2
w1 = Matrix([0, 0, 1])
w2 = Matrix([0, 1/sqrt(2), -1/sqrt(2)])

# Define the skew-symmetric matrix computation function
def skew_symmetric(w):
    return Matrix([
        [0, -w[2], w[1]],
        [w[2], 0, -w[0]],
        [-w[1], w[0], 0]
    ])

# Compute skew-symmetric matrices for w1 and w2
w1_skew = skew_symmetric(w1)
w2_skew = skew_symmetric(w2)

# Define theta1 and theta2
theta1, theta2 = symbols('theta1 theta2')

# Compute the rotation matrices for w1 and w2 symbolically
R_w1_symbolic = Matrix.eye(3) + sin(theta1) * w1_skew + (1 - cos(theta1)) * (w1_skew * w1_skew)
R_w2_symbolic = Matrix.eye(3) + sin(theta2) * w2_skew + (1 - cos(theta2)) * (w2_skew * w2_skew)

# Compute the combined rotation matrix
R_combined_symbolic = R_w1_symbolic * R_w2_symbolic

print(w1_skew)
print(w2_skew)

print(R_w1_symbolic)
print(R_w2_symbolic)

print(R_combined_symbolic)

import sympy as sp

# Define the target matrix R
R_target = Matrix([
    [1/sqrt(2), 0, -1/sqrt(2)],
    [0, 1, 0],
    [1/sqrt(2), 0, 1/sqrt(2)]
])

# Modified the code to handle the situation where no solution is found

try:
    # Equate elements of R_combined_symbolic and R_target to create equations
    equations = [sp.Eq(R_combined_symbolic[i, j], R_target[i, j]) for i in range(3) for j in range(3)]
    
    # Solve the system of equations for theta1 and theta2
    solutions = sp.solve(equations, (theta1, theta2), dict=True)
    
    # Display the solutions
    if solutions:
        solution_found = True
    else:
        solution_found = False

except Exception as e:
    solution_found = False
    error_message = str(e)

print(solution_found, solutions if solution_found else "No solutions found")

# Equate elements of R_combined_symbolic and R_target to create equations
equations = [sp.Eq(R_combined_symbolic[i, j], R_target[i, j]) for i in range(3) for j in range(3)]

# Solve the system of equations for theta1 and theta2
solutions = sp.solve(equations, (theta1, theta2), dict=True)

# Display the solutions
print(solutions)