import os
import re

file = open(r'D:\medic\task20200916\mut_result.gen.txt','r',encoding='UTF-8')

lines = file.readlines()
file.close()
#lines = ["	<category=GEN>TAT</category></category></category></category>, median <category=GEN><category=GEN>(SEM)</category>, d	73.1 (2.1)	95.0 (1.5)	51.1 (3.2)	13.0 (0.4)	NA	<.001c"]
targets = {}
for line in lines:
    string = line.strip()
    target = re.findall('<category=GEN>(.*?)</category>',string,re.S)
    for tg in target:
        if tg in targets:
            targets[tg] +=1 
        else:
            targets[tg] = 1
string = ""
for tg in targets:
    string += str(tg)+'\t'+str(targets[tg])+'\n'
file = open('./result.txt','w',encoding='utf-8')
file.writelines(string)
file.close()
