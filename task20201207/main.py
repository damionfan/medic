# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/12/7 15:27
# software: PyCharm
# function : None


import os
import re

file = open('./new.txt', 'r', encoding='utf-8')
sections = file.readlines()
file.close()
gen_set = dict()
mu_set = dict()
gen = re.compile(r'<category=GEN>(.*?)</category>', re.S)
mutation = re.compile(r'<category=mutation>(.*?)</category>', re.I)
gi = 0
mi = 0
file = open('./new_ids.txt', 'w', encoding='utf-8')
for section in sections:
    lines = section.strip().split('. ')
    for id, line in enumerate(lines):
        gs = gen.findall(line)
        ms = mutation.findall(line)
        for ids, g in enumerate(set(gs)):
            index_list = [i.start() for i in re.finditer(g, line.strip())]
            for i, l in enumerate(index_list):
                line = line[:l + i * (len(g) - 1)] + g + '<ID :' + str(i) + ">" + line[l + i * (len(g) - 1) + len(g):]

        for ids, m in enumerate(set(ms)):
            index_list = [i.start() for i in re.finditer(m, line.strip())]
            for i, l in enumerate(index_list):
                line = line[:l + i * (len(m) - 1)] + m + '<ID :' + str(i) + ">" + line[l + i * (len(m) - 1) + len(m):]

            if m not in mu_set:
                mu_set[m] = 0
            else:
                mu_set[m] += 1
        file.writelines('\n' + str(id) + ' ' + line.strip())

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

# for m in mu_set.keys():
for section in sections:
    lines_up = section.strip().split('. ')
    for id, li in enumerate(lines_up):
        # gs = gen.findall(line)
        ms = mutation.findall(li)
        for _, m in enumerate(set(ms)):
            index = lines_up.index(li)
            index_list = [i.start() for i in re.finditer(m, li.strip())]
            for ids, _ in enumerate(index_list):
                file.writelines('\n' + 'Lines:' + str(id) + ' ' + m + ' ID: ' + str(ids) + '\n')
                mu_dic = dict()
                for si, section in enumerate(sections):
                    lines = section.strip().split('. ')
                    for i, line2 in enumerate(lines):
                        gs = gen.findall(line2.strip())
                        for _, g in enumerate(set(gs)):
                            index_list = [i.start() for i in re.finditer(g, line2.strip())]
                            for ids, _ in enumerate(index_list):
                                print(i, index)

                                mu_dic["{}-({}-L:{}-ID:{})".format(m, g, i, ids)] = (abs(index - i))

                                # print(str(abs(index-i))+'-'+mu_set[m] + '-' + gen_set[g])

                mu_dic = sorted(mu_dic.items(), key=lambda d: d[1], reverse=False)
                # print(mu_dic)
                for mu in mu_dic:
                    file.writelines(str(mu[1]) + '-' + mu[0] + '\n')
file.close()
