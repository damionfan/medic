
string = '\n'
file = open('task20201010/test.tsv','r',encoding='utf-8')
lines = file.readlines()
string = '\n'
for line in lines:
    if len(line.strip('\n')) == 0:
        string += '\n'
    else:
        words = line.strip().split('\t')
        #if words[1] != 'O':
        string += words[0]+' '+words[1]+'\n'
file.close()

file = open('task20201010/v2/NCBI/test.txt','w',encoding='utf-8')
file.writelines(string)
file.close()