import numpy as np
from tkinter import *
import tkinter.font as tf


# min


def function(flag, txt, a):
    # flag = 'max'
    # flag = 'min'
    ft = tf.Font(family='微软雅黑', size=10)  ###有很多参数
    txt.tag_add('tag', END)  # 申明一个tag,在a位置使用
    txt.tag_config('tag', foreground='blue', background='pink', font=ft)  # 设置tag即插入文字的大小,颜色等

    txt.tag_add('tag1', END)  # 申明一个tag,在a位置使用
    txt.tag_config('tag1', foreground='green', font=ft)  # 设置tag即插入文字的大小,颜色等

    all_matrix = a[1:]  # np.array([[1, 1, -2, 1, 0, 0, 10], [2, -1, 4, 0, 1, 0, 8], [-1, 2, -4, 0, 0, 1, 4]])
    # print(all_matrix)
    obj = a[0][:-1]  # np.array([1, -2, 1, 0, 0, 0])
    num = 0
    # value = np.ones((1, all_matrix.shape[0] - 1))
    # 选择的x

    zero_size = sum(obj == 0)
    # print(zero_size, range(obj.shape[0] - zero_size))
    seclet_index = np.array(range(obj.shape[0] - zero_size, obj.shape[0]))  # np.array([3, 4, 5])
    # print(seclet_index)
    #
    cb = np.zeros((zero_size, 1))
    final_value = 0.0
    end = False

    while not end:

        # print("step:", num)
        s = 'Step :%s\n\n' % (str(num))
        txt.insert(END, s, 'tag1')
        num += 1
        # print(all_matrix)

        s = 'Matrix :\n%s\n' % (str(all_matrix))
        txt.insert(END, s, 'tag')
        results = all_matrix[:, -1]

        matrix = all_matrix[:, :-1]

        # print(cb)
        for i, j in enumerate(seclet_index):
            cb[i] = obj[j]

        value = np.matmul(cb.T, matrix) - obj
        # print("value", value)
        s = 'Value :\n%s\n' % (str(value))
        txt.insert(END, s, 'tag1')
        # print('final_value:', final_value)
        s = 'Final_value :%s\n' % (str(final_value))
        txt.insert(END, s, 'tag')
        # fv = final_value
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


