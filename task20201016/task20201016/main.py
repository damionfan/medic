# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/11/27 18:07
# software: PyCharm
# function : None

from tkinter import *
import numpy as np
import json

from PIL import ImageTk, Image

from task20201016.danchunxing import function
from task20201016.TransportationProblem import transportation_problem as tp


def run1():
    txt.delete(0.0, END)
    r1 = Tk()
    r1.geometry('300x300')
    r1.title('最优化输入')
    la = Label(r1, text="请在下面的文本框中\n输入单纯形约束矩阵", font=('Arial 12 bold'), width=20, height=5)
    la.place(x=50, y=0)
    r1.resizable(width=False, height=False)
    t1 = Text(r1, width=100, height=10)
    t1.place(x=0, y=100)

    def getmatrix():
        matrix = t1.get("0.0", "end")
        ma = []

        matrixs = matrix.strip(' ').split('\n')
        for m in matrixs:
            if len(m) > 1:
                ma.append(list(map(float, m.split('\t'))))
        matrix = np.array(ma)
        function('min', txt, matrix)
        r1.destroy()
        return matrix

    button = Button(r1, text="提交", command=getmatrix, width=10, height=2)  # command绑定获取文本框内容方法
    button.place(x=100, y=245)
    r1.mainloop()


def run2():
    txt.delete(0.0, END)
    r1 = Tk()
    r1.geometry('300x300')
    r1.title('最优化输入')
    la = Label(r1, text="请在下面的文本框中\n输入单纯形约束矩阵", font=('Arial 12 bold'), width=20, height=5)
    la.place(x=50, y=0)
    r1.resizable(width=False, height=False)
    t1 = Text(r1, width=100, height=10)
    t1.place(x=0, y=100)

    def getmatrix():
        matrix = t1.get("0.0", "end")
        ma = []

        matrixs = matrix.strip(' ').split('\n')
        for m in matrixs:
            if len(m) > 1:
                ma.append(list(map(float, m.split('\t'))))
        matrix = np.array(ma)
        function('max', txt, matrix)
        r1.destroy()
        return matrix

    button = Button(r1, text="提交", command=getmatrix, width=10, height=2)  # command绑定获取文本框内容方法
    button.place(x=100, y=245)
    r1.mainloop()


def run3():
    txt.delete(0.0, END)
    r1 = Tk()
    r1.geometry('300x350')
    r1.title('运输问题条件设置')
    r1.resizable(width=False, height=False)
    la1 = Label(r1, text="A:", font=('Arial', 15), width=2, height=2)
    la1.place(relx=0.1, rely=0.06)
    t1 = Text(r1, width=30, height=2)
    t1.place(relx=0.2, rely=0.1)

    la2 = Label(r1, text="B:", font=('Arial', 15), width=2, height=2)
    la2.place(relx=0.1, rely=0.26)
    t2 = Text(r1, width=30, height=2)
    t2.place(relx=0.2, rely=0.3)

    la3 = Label(r1, text="Cost:", font=('Arial', 15), width=6, height=2)
    la3.place(relx=0., rely=0.46)
    t3 = Text(r1, width=30, height=8)
    t3.place(relx=0.2, rely=0.5)

    def getmatrix():
        av = t1.get("0.0", "end")

        aa = av.strip(' ')
        a = (list(map(float, aa.split('\t'))))
        a = np.array(a)

        bv = t2.get("0.0", "end")

        bb = bv.strip(' ')
        b = (list(map(float, bb.split('\t'))))
        b = np.array(b)

        matrix = t3.get("0.0", "end")
        ma = []

        matrixs = matrix.strip(' ').split('\n')
        for m in matrixs:
            if len(m) > 1:
                print(m.split("\t"))
                ma.append(list(map(float, m.split('\t'))))
        c = np.array(ma)

        # print(a,b,c)

        # a = np.loadtxt('a.txt')
        s = []
        for i, n in enumerate(a):
            s.append(('A' + str(i + 1), n))
        # print(s)

        # b = np.loadtxt('b.txt')
        d = []
        for i, n in enumerate(b):
            d.append(('B' + str(i + 1), n))
        # print(d)

        # c = np.loadtxt('tp.txt')
        # print(a,b,c)
        # 初始化运输问题对象
        p = tp.TransportationProblem(s, d, c)
        # 求解，使用西北角法初始化，位势法检验，闭回路法优化调整
        r = p.solve(tp.NorthwestCornerIniter, tp.PotentialChecker, tp.ClosedLoopAdjustmentOptimizer)

        # 输出解
        # 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框

        s = '产地、产量:\n%s\n目的地、销量:\n%s\n运价表:\n%s\n%s\n' % (str(s), str(d), str(c), str(r))
        txt.insert(END, s)

        r1.destroy()
        return a, b

    button = Button(r1, text="提交", command=getmatrix, width=10, height=2)  # command绑定获取文本框内容方法
    button.place(x=100, y=290)
    r1.mainloop()


root = Tk()
root.geometry('800x400')
root.title('最优化')
root.resizable(width=False, height=False)
canvas = Canvas(root, width=800, height=400)
imgpath = 'background.jpg'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)

canvas.create_image(100, 280, image=photo)
canvas.pack()

# 方法-直接调用 run1()
btn1 = Button(root, text='单纯形最小值', command=run1, width=20, height=2)
btn1.place(x=10, y=20)

# 方法二利用 lambda 传参数调用run2()
btn2 = Button(root, text='单纯形最大值', command=lambda: run2(), width=20, height=2)
btn2.place(x=10, y=80)

btn3 = Button(root, text='运输问题', command=lambda: run3(), width=20, height=2)
btn3.place(x=10, y=140)

txt = Text(root)

scroll = Scrollbar()
# 放到窗口的右侧, 填充Y竖直方向
scroll.pack(side=RIGHT, fill=Y)

# 两个控件关联
scroll.config(command=txt.yview)
txt.config(yscrollcommand=scroll.set)
txt.place(x=200, y=10)

root.mainloop()
