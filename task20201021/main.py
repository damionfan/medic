sx_table = {'0':'c','1':'5','2':'6','3':'b','4':'9','5':'0','6':'a','7':'d','8':'3','9':'e','a':'f','b':'8','c':'4','d':'7','e':'1','f':'2'}
new_table = {v : k for k, v in table.items()}
#print(new_table)

def sx(number_16):
    new_str ='0x'
    for i in '{:0>4}'.format(number_16[2:]):
        new_str += sx_table[i]
    return new_str

def back_sx(number_16):
    new_str ='0x'
    for i in '{:0>4}'.format(number_16[2:]):
        new_str += new_table[i]
    return new_str

def player(number_16):
    a = ''
    b = ''
    c = ''
    d = ''
    for i in number_16[2:]:
        new = '{:0>4}'.format(str(bin(int(i,16))[2:]))
        a += new[0]
        b += new[1]
        c += new[2]
        d += new[3]
    return str(hex(int(a+b+c+d,2)))


def xor(byte1, byte2):  
    return hex(byte1 ^ byte2)

def loop_left_move(key):
    key = '{:0>16}'.format(str(bin(int(key,16)))[2:])
    key = key[7:]
    low = key[:7]
    return str(hex(int(key+low,2)))

def loop_right_move(key):
    key = '{:0>16}'.format(str(bin(int(key,16)))[2:])
    key = key[-7:]
    low = key[:-7]
    
    return str(hex(int(key+low,2)))

def iter_for(input,key):
    p = input
    for i in range(15):
        new = '0x'
        new += '{:0>4}'.format(xor(int(p,16),int(key,16))[2:])
        p = sx(new)
        p = player(p)
        key = loop_left_move(key)
    new = '0x'
    new += '{:0>4}'.format(xor(int(p,16),int(key,16))[2:])
    return str(new) 


def iter_back(input,key):
    p = input
    new = '0x'
    new += '{:0>4}'.format(xor(int(p,16),int(key,16))[2:])
    for i in range(15):
        p = player(new)
        p = back_sx(p)
        new = '0x'
        key = loop_right_move(key)
        new += '{:0>4}'.format(xor(int(p,16),int(key,16))[2:])
    return str(new),key 


def get_index(lst=None, item=''):
    return [index for (index,value) in enumerate(lst) if value == item]




"""
Algorithm Start: 
"""
source = ['0x9527','0x3322','0xcdaf']
target = ['0xce5e','0x006c','0xfc67']

key1_val = []
key2_val = []
"""
search all value of (0x00-0xff) for the first group 
"""
for i in range(65536):
    result2, _ = iter_back(target[0],'0x'+'{:0>4}'.format(str(hex(i))[2:]))
    result1 = iter_for(source[0],'0x'+'{:0>4}'.format(str(hex(i))[2:]))  
    key1_val.append(result1)
    key2_val.append(result2)




key1 = []
key2 = []
"""
To get the same value bases on key1_val and key2_val
"""
same_value = set(key1_val)&set(key2_val)
for i in same_value:
    b = get_index(key2_val,i)
    a = get_index(key1_val,i)
    
    for m in a:
        for n in b:
            key2.append(n)
            key1.append(m)
            

k1 = []
k2 = []

"""
Search for second group
"""
for i in range(len(key1)):
    result2,_ = iter_back(target[1],'0x'+'{:0>4}'.format(str(hex(key2[i]))[2:]))
    result1 = iter_for(source[1],'0x'+'{:0>4}'.format(str(hex(key1[i]))[2:]))
    
    if  result1 == result2 :
        k2.append(key2[i])
        k1.append(key1[i])
        
key1 = k1
key2 = k2

k1 = []
k2 = []

"""
Finall 
"""

for i in range(len(key1)):
    result1 = iter_for(source[2],'0x'+'{:0>4}'.format(str(hex(key1[i]))[2:]))
    result2,k = iter_back(target[2],'0x'+'{:0>4}'.format(str(hex(key2[i]))[2:]))
    if result1 == result2:
        k1.append(key1[i])
        """
        We need to get 10-bit value for the key2,transformer
        """
        k2.append(int(k,16))
key1 = k1
key2 = k2


"""
Result:
"""
for i in range(len(key1)):
    print("Key1:\t",key1[i],'Key2:\t',key2[i])


