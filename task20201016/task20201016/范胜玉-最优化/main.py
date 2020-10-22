# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/11/27 18:07
# software: PyCharm
# function : None

from tkinter import *
import numpy as np

from task20201016.danchunxing import function
from task20201016.TransportationProblem import transportation_problem as tp


def run1():
    txt.delete(0.0, END)
    function('min', txt)


def run2():
    txt.delete(0.0, END)
    function('max', txt)


def run3():
    txt.delete(0.0, END)
    a = np.loadtxt('a.txt')
    s = []
    for i, n in enumerate(a):
        s.append(('A' + str(i + 1), n))
    print(s)

    b = np.loadtxt('b.txt')
    d = []
    for i, n in enumerate(b):
        d.append(('B' + str(i + 1), n))
    print(d)

    c = np.loadtxt('tp.txt')

    # 初始化运输问题对象
    p = tp.TransportationProblem(s, d, c)
    # 求解，使用西北角法初始化，位势法检验，闭回路法优化调整
    r = p.solve(tp.NorthwestCornerIniter, tp.PotentialChecker, tp.ClosedLoopAdjustmentOptimizer)

    # 输出解
    # 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框

    scroll = Scrollbar()
    # 放到窗口的右侧, 填充Y竖直方向
    scroll.pack(side=RIGHT, fill=Y)

    # 两个控件关联
    scroll.config(command=txt.yview)
    txt.config(yscrollcommand=scroll.set)
    txt.place(rely=0.5, relheight=0.4)
    s = '产地、产量%s\n目的地、销量%s\n运价表:\n%s\n%s\n' % (str(s), str(d), str(c), str(r))
    txt.insert(END, s)


root = Tk()
root.geometry('700x800')
root.title('最优化')

# 方法-直接调用 run1()
btn1 = Button(root, text='单纯形最小值：', command=run1)
btn1.place(relx=0.1, rely=0, relwidth=0.3, relheight=0.1)

# 方法二利用 lambda 传参数调用run2()
btn2 = Button(root, text='单纯形最大值：', command=lambda: run2())
btn2.place(relx=0.6, rely=0, relwidth=0.3, relheight=0.1)

btn3 = Button(root, text='运输问题', command=lambda: run3())
btn3.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.1)

# 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框
txt = Text(root)

scroll = Scrollbar()
# 放到窗口的右侧, 填充Y竖直方向
scroll.pack(side=RIGHT, fill=Y)

# 两个控件关联
scroll.config(command=txt.yview)
txt.config(yscrollcommand=scroll.set)
txt.place(rely=0.5)

root.mainloop()
