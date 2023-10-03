import numpy as np
np.set_printoptions(suppress=True)

# Define the rotation matrices for Rot(x, pi/2) and Rot(z, pi)
rot_x = np.array([[1, 0, 0],
                  [0, np.cos(np.pi/2), -np.sin(np.pi/2)],
                  [0, np.sin(np.pi/2), np.cos(np.pi/2)]])

rot_z = np.array([[np.cos(np.pi), -np.sin(np.pi), 0],
                  [np.sin(np.pi), np.cos(np.pi), 0],
                  [0, 0, 1]])

# Compute the product of the two rotation matrices
R = np.dot(rot_x, rot_z)

print(rot_x)
print(rot_z)
print(R)

# First, find the eigenvalues and eigenvectors of R
eigenvalues, eigenvectors = np.linalg.eig(R)

# The axis of rotation corresponds to the eigenvector for the eigenvalue 1
axis_of_rotation = eigenvectors[:, np.isclose(eigenvalues, 1)].flatten()

# Now, find the angle of rotation using the trace of R
angle_of_rotation_rad = np.arccos((np.trace(R) - 1) / 2)

# Convert angle of rotation to degrees for easier interpretation
angle_of_rotation_deg = np.degrees(angle_of_rotation_rad)

print(axis_of_rotation)
print(angle_of_rotation_deg)
