import numpy as np

# min

flag = 'max'
# flag = 'min'

all_matrix = np.array([[1, 1, 2, 1, 0, 6], [1, 4, -1, 0, 1, 4]])
print(all_matrix)
obj = np.array([2, 1, -1, 0, 0])
num = 0
value = np.ones((1, all_matrix.shape[0] - 1))
# 选择的x
seclet_index = np.array([3, 4])

#
cb = np.zeros((2, 1))
final_value = 0.0
end = False


while not end:

    print("step:", num)
    num += 1
    print(all_matrix)

    results = all_matrix[:, -1]

    matrix = all_matrix[:, :-1]

    # print(cb)
    for i, j in enumerate(seclet_index):
        cb[i] = obj[j]

    value = np.matmul(cb.T, matrix) - obj
    print("value", value)
    print('final_value:', final_value)
    final_value = 0.0
    if np.max(value) <= 0:
        break
    # obj-min -> value -max
    if flag == 'min':
        j_index = value.tolist()[0].index(max(value.tolist()[0]))
        if np.max(value) <= 0:
            end = True
    elif flag == 'max':
        j_index = value.tolist()[0].index(min(value.tolist()[0]))
        if np.min(value) >= 0:
            end = True
    # print('j_index', value.tolist()[0].index(max(value.tolist()[0])))

    y = []
    for i, r in enumerate(results):
        if matrix[:, j_index][i] > 0:
            y.append(results[i] / matrix[:, j_index][i])
        else:
            y.append(9999)

    i_index = y.index(min(y))
    seclet_index[i_index] = j_index

    all_matrix = all_matrix.astype(np.float64)
    all_matrix[i_index] = all_matrix[i_index] / all_matrix[i_index][j_index]

    for i in range(all_matrix.shape[0]):
        if i is not i_index:
            all_matrix[i] = all_matrix[i] - all_matrix[i][j_index] * all_matrix[i_index]
    # print(all_matrix)

    results = all_matrix[:, -1]

    for i, va in enumerate(seclet_index):
        final_value += results[i] * obj[va]
