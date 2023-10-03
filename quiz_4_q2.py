import numpy as np

# Given matrix R
R_given = np.array([[0, -1, 0],
                    [0, 0, -1],
                    [1, 0, 0]])

# Check orthogonality
is_orthogonal = np.allclose(np.dot(R_given.T, R_given), np.eye(3))

# Check determinant
determinant = np.linalg.det(R_given)

print(is_orthogonal)
print(determinant)

print(determinant == 1)


# Compute the angle of rotation theta
theta = np.arccos((np.trace(R_given) - 1) / 2)

# Compute the components of the axis of rotation w
w = np.array([
    (R_given[2, 1] - R_given[1, 2]) / (2 * np.sin(theta)),
    (R_given[0, 2] - R_given[2, 0]) / (2 * np.sin(theta)),
    (R_given[1, 0] - R_given[0, 1]) / (2 * np.sin(theta))
])

angle_of_rotation_deg = np.degrees(theta)
# Now, compute the exponential coordinates w.theta
exp_coordinates = w * theta
print(w)
print(exp_coordinates)
print(theta)
print(angle_of_rotation_deg)


