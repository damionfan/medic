# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/12/7 21:46
# software: PyCharm
# function : None

import os

file = open('./28288113.txt.gen.mut', 'r', encoding='utf-8')
lines = file.readlines()
file.close()
lines = list(filter(lambda x: x != '\n', lines))
string = ' '.join(lines).replace('\n', '.')
file = open('./new.txt', 'w', encoding='utf-8')
file.writelines(string)
file.close()
