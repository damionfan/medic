# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/12/7 15:27
# software: PyCharm
# function : None


import os
import re

file = open('././28288113.txt.gen.mut', 'r', encoding='utf-8')
sections = file.readlines()
file.close()
gen_set = dict()
mu_set = dict()
gen = re.compile(r'<category=GEN>(.*?)</category>', re.S)
mutation = re.compile(r'<category=mutation>(.*?)</category>', re.I)
gi = 0
mi = 0
file = open('./new_ids.txt', 'w', encoding='utf-8')
for sid, section in enumerate(sections):
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
        file.writelines('\n' + 'Para:{} Line:{}\t'.format(sid, id) + ' ' + line.strip())
    file.writelines('\n')
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
for secid, section in enumerate(sections):
    lines_up = section.strip().split('. ')
    for id, li in enumerate(lines_up):
        # gs = gen.findall(line)
        ms = mutation.findall(li)
        for _, m in enumerate(set(ms)):
            index = lines_up.index(li)
            index_list = [i.start() for i in re.finditer(m, li.strip())]
            for ids, _ in enumerate(index_list):
                file.writelines(
                    '\n{} (Paragraph: {} Line: {} ID: {} )\nDistance,\t\t\tMutation,\t\t\tGene(Paragraph-Line-ID)\t\t'.format(
                        m, secid, id, ids))
                mu_dic_l = dict()
                mu_dic_p = dict()
                for si, section in enumerate(sections):
                    lines = section.strip().split('. ')
                    for i, line2 in enumerate(lines):
                        gs = gen.findall(line2.strip())
                        for _, g in enumerate(set(gs)):
                            index_list = [i.start() for i in re.finditer(g, line2.strip())]
                            for ids, _ in enumerate(index_list):
                                if secid == si:
                                    mu_dic_l["{},\t\t\t{} ({}, {}, ID:{})".format(m, g, si, i, ids)] = (abs(index - i))
                                else:
                                    mu_dic_p["{},\t\t\t{} ({}, {}, ID:{}) ".format(m, g, si, i, ids)] = (
                                        abs(secid - si))
                                # print(str(abs(index-i))+'-'+mu_set[m] + '-' + gen_set[g])

                mu_dic_l = sorted(mu_dic_l.items(), key=lambda d: d[1], reverse=False)
                for mu in mu_dic_l:
                    file.writelines('\n{} lines,\t\t\t{}'.format(str(mu[1]), mu[0]))

                mu_dic_p = sorted(mu_dic_p.items(), key=lambda d: d[1], reverse=False)

                for mu in mu_dic_p[:5]:
                    file.writelines('\n{} paragraphs,\t\t{}'.format(str(mu[1]), mu[0]))
                file.writelines('\n\n')

file.close()

'''
Para:58 Line:0 Input data

c.C388T(Paragraph: 205 Line: 3 ID: 0 )
  Distance,             Mutation,      Gene(Paragraph, Line, ID)  
  0 lines,                 c.C388T,        SMS (205, 3, ID: 0)
  1 lines,                 c.C388T,        LGALS9C (205, 4, ID:0)
  4 paragraphs,       c.C388T        SMS(201, 0, ID:0)
'''
