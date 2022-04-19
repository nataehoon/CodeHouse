import numpy as np

a1 = np.array([1, 2, 3, 4, 5])
# print(a1)
# print(type(a1))
# print(a1.shape)
# print(a1[0], a1[1], a1[2], a1[3], a1[4])
# a1[0] = 4
# a1[1] = 5
# a1[2] = 6
# print(a1)

a2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
# print(a2)
# print(a2.shape)
# print(a2[0, 0], a2[1, 1], a2[2, 2])

a3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
# print(a3)
# print(a3.shape)

# print(np.zeros(10))
# print(np.ones(10))
# print(np.ones((3, 3)))
# print(np.full((3, 3), 1.23))

# print(np.eye(3))
# print(np.tri(3))
# print(np.empty(10))

# print(np.zeros_like(a1))
# print(np.ones_like(a2))
# print(np.full_like(a3, 10))

# print(np.arange(0, 30, 2))
# print(np.linspace(0, 1, 5))
# print(np.logspace(0.1, 1, 20))

print(np.random.random((3, 3)))
print(np.random.randint(0, 10, (3, 3)))
print(np.random.normal(0, 1, (3, 3)))
print(np.random.rand(3, 3))
print(np.random.randn(3, 3))