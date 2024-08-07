import numpy as np

# solving for x and y in 
# 4x + 7y = 8
# 5x + 7y = 9
A = np.array([[4, 7],
              [5, 7]])
B= np.array([8, 9])
x = np.linalg.solve(A, B)
print(x)