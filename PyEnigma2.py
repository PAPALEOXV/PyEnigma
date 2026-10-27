byte0=int(input())
name2=input()
name3=input()
data3=[]
with open('PyEnigma1',mode='rb')as file:
    data0=file.read()
with open('PyEnigma2',mode='rb')as file:
    data1=file.read()
with open(name2,mode='rb')as file:
    data2=file.read()
for byte2 in data2:
    if byte2>125:
        byte2-=7
    elif byte2>96:
        byte2-=4
    elif byte2>64:
        byte2-=2
    elif byte2>37:
        byte2-=1
    byte2-=32
    byte3=data1[byte2]
    if byte3>125:
        byte3-=7
    elif byte3>96:
        byte3-=4
    elif byte3>64:
        byte3-=2
    elif byte3>37:
        byte3-=1
    byte3-=data0[byte0]
    while byte3<32:
        byte3+=88
    byte0+=1
    while byte0>87:
        byte0-=88
    if byte3>118:
        byte3+=7
    elif byte3>92:
        byte3+=4
    elif byte3>62:
        byte3+=2
    elif byte3>36:
        byte3+=1
    data3.append(byte3)
with open(name3,mode='wb')as file:
    file.write(bytes(data3))