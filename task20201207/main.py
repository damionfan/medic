# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/12/7 15:27
# software: PyCharm
# function : None


import os
import re

file = open('./28288113.txt.gen.mut', 'r', encoding='utf-8')
sections = file.readlines()
file.close()
gen_set = dict()
mu_set = dict()
gen = re.compile(r'<category=GEN>(.*?)</category>', re.S)
mutation = re.compile(r'<category=mutation>(.*?)</category>', re.S)
gi = 0
mi = 0
for section in sections:
    lines = section.strip().split('. ')
    for line in lines:
        gs = gen.findall(line)
        ms = mutation.findall(line)
        for g in gs:
            if g not in gen_set:
                gen_set[g] = 'G' + str(gi)
                gi += 1
        for m in ms:
            if m not in mu_set:
                mu_set[m] = 'M' + str(mi)
                mi += 1
# print(gen_set)
# print(mu_set)
file = open('./result.txt', 'w', encoding='utf-8')
'''
file.writelines('GEN\n')
for g in gen_set:
    file.writelines(g + '-' + gen_set[g] + '  ')
file.writelines('\nMutation\n')
for g in mu_set:
    file.writelines(g + '-' + mu_set[g] + '  ')
file.writelines('\n\n')
'''

for m in mu_set.keys():
    print(m)
    file.writelines('\n'+m+'\n')
    mu_dic = dict()
    for si, section in enumerate(sections):
        lines = section.strip().split('. ')
        L_length = len(lines)
        for line in lines:
            if m in line:
                index = lines.index(line)
                for i, line2 in enumerate(lines):
                    gs = gen.findall(line2.strip())
                    for g in gs:
                        if m + '-' + g not in mu_dic:
                            mu_dic[m + '-' + g] = str(abs(index - i))
                        else:
                            if mu_dic[m + '-' + g] > str(abs(index - i)):
                                mu_dic[m + '-' + g] = str(abs(index - i))
                        # print(str(abs(index-i))+'-'+mu_set[m] + '-' + gen_set[g])
    for mu in mu_dic.keys():
        file.writelines(mu_dic[mu]+'-'+mu+'\n')
