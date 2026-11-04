import numpy as np

# list = [70, 72, 71]
# print(list * 2)
# print([v * 2 for v in list])

# temp = np.array([70, 72, 71])
# print(temp)
# print(temp * 2)

# print(np.array((1, 2, 3))) ### 튜플로도 출력가능

# temp = np.array([32, 44, 55, 33, 57])
# print(temp)
# print(temp * 1.8 + 32)

# # 실습 2
# current = np.arange(0, 80, 10)
# print(current)

# # 실습 3
# idx = np.arange(0, 40, 5)
# print(idx)

# # 실습 4
# idx = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# print("차원:", idx.ndim)
# print("형태:", idx.shape)
# print("개수:", idx.size)
# print("자료형:", idx.dtype, '\n')

# # 실습 5
# current = np.array([1.4, 2.5, 3.8, 4.1])
# current_float = current.astype(int)
# print("자료형:", current.dtype)
# print("원본:", current)
# print("정수화:", current_float)

# # 실습 6
# value = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(value.reshape(3,4))
# print(value.reshape(4,3))
# print(value)

# # 실습 7
# value = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# line = value.reshape(4,3)
# print(line)
# back = line.flatten()
# print(back)
# print((value == back).all())

##############################################################################################

# 실습 1
value = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(value[0], value[-1])
print(value[1 : 5])
print(value[:: 2])

# 실습 2
a = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(a[2]) ### 2행 출력
print(a[:, 0]) ### 0열 출력
print(a[:, 1]) ### 1열 출력