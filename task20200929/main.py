import os


file = open('./task20200929/single_cell_Beaudet-31785788.txt','r',encoding='utf-8')
lines = file.readlines()
file.close()
file = open('./task20200929//result.txt','w',encoding='utf-8')
for line in lines:
    words = line.strip().split(' ')
    for word in words:
        if len(word) > 0:
            print(word)
            if word[0] == '(' and word[-1]==')':
                file.writelines(word[0]+' O\n')
                file.writelines(word[1:-1]+' O\n')
                file.writelines(word[-1]+' O\n')
            elif word[-1] == '.' :
                file.writelines(word[:-1]+' O\n')
                file.writelines(word[-1]+' O\n')
                file.writelines('\n')
            elif word[-1] == ',':
                file.writelines(word[:-1]+' O\n')
                file.writelines(word[-1]+' O\n')
            else:
                file.writelines(word+' '+'O\n')
    file.writelines('\n')
file.close()
