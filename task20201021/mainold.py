table = {'0':'c','1':'5','2':'6','3':'b','4':'9','5':'0','6':'a','7':'d','8':'3','9':'e','a':'f','b':'8','c':'4','d':'7','e':'1','f':'2'}
new_table = {v : k for k, v in table.items()}
#print(new_table)

def sx(number_hex):
    new_str ='0x'
    for i in '{:0>4}'.format(number_hex[2:]):
        new_str += table[i]
    return new_str

def back_sx(number_hex):
    new_str ='0x'
    
    for i in '{:0>4}'.format(number_hex[2:]):
        new_str += new_table[i]
    return new_str

def player(number_hex):
    a = ''
    b = ''
    c = ''
    d = ''
    for i in number_hex[2:]:
        new = '{:0>4}'.format(str(bin(int(i,16))[2:]))
        a += new[0]
        b += new[1]
        c += new[2]
        d += new[3]
    return str(hex(int(a+b+c+d,2)))


def x_o_r(byte1, byte2):  
    return hex(byte1 ^ byte2)

def loop_left_move(key):
    key = '{:0>16}'.format(str(bin(int(key,16)))[2:])
    low = key[:7]
    key = key[7:]
    return str(hex(int(key+low,2)))

def loop_right_move(key):
    key = '{:0>16}'.format(str(bin(int(key,16)))[2:])
    low = key[:-7]
    key = key[-7:]
    return str(hex(int(key+low,2)))

def iter_forward(input,key):
    p = input
    for i in range(15):
        new = '0x'
        new += '{:0>4}'.format(x_o_r(int(p,16),int(key,16))[2:])
        key = loop_left_move(key)
        p = sx(new)
        p = player(p)
    new = '0x'
    new += '{:0>4}'.format(x_o_r(int(p,16),int(key,16))[2:])
    return str(new) 


def iter_backward(input,key):
    p = input
    # print(input,key)
    new = '0x'
    new += '{:0>4}'.format(x_o_r(int(p,16),int(key,16))[2:])
    for i in range(15):
        p = player(new)
        p = back_sx(p)
        key = loop_right_move(key)
        new = '0x'
        new += '{:0>4}'.format(x_o_r(int(p,16),int(key,16))[2:])
    return str(new) 

def epoch(input,key1,key2):
    o1 = iter(input,key1)
    o2 = iter(o1,key2)

    return o2

def get_index1(lst=None, item=''):
    return [index for (index,value) in enumerate(lst) if value == item]

def main():
    source = ['0x9527','0x3322','0xcdaf']
    target = ['0xce5e','0x006c','0xfc67']

    key1_val = []
    key2_val = []
    for i in range(65536):
        key1_val.append(iter_forward(source[0],'0x'+'{:0>4}'.format(str(hex(i))[2:])))
        key2_val.append(iter_backward(target[0],'0x'+'{:0>4}'.format(str(hex(i))[2:])))
    
    same_val = set(key1_val)&set(key2_val)


    key1 = []
    key2 = []
    for i in same_val:
        key1.append(key1_val.index(i))
        key2.append(key2_val.index(i))
    
    k1 = []
    k2 = []
    for i in range(len(key1)):
        
        result1 = iter_forward(source[1],'0x'+'{:0>4}'.format(str(hex(key1[i]))[2:]))
        result2 = iter_backward(target[1],'0x'+'{:0>4}'.format(str(hex(key2[i]))[2:]))
        # print(result1,result2)
        if  result1 == result2 :
            k1.append(key1[i])
            k2.append(key2[i])
    key1 = k1
    key2 = k2
    print(key1,key2)

    k1 = []
    k2 = []
    for i in range(len(key1)):
        if iter_forward(source[2],'0x'+'{:0>4}'.format(str(hex(key1[i]))[2:])) == iter_backward(target[2],'0x'+'{:0>4}'.format(str(hex(key2[i]))[2:])):
            k1.append(key1[i])
            k2.append(key2[i])
    key1 = k1
    key2 = k2


    print(key1,key2)


        
    
    
if __name__ == "__main__":
   main()

    #print(iter_backward('0xce5e','0x253b'))
