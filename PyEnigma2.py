byte0=int(input())
byte1=int(input())
name2=input()
name4=input()
data4=[]
with open('PyEnigma4',mode='rb')as file:
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
    byte3=data0[byte2]
    if byte2>125:
        byte2-=7
    elif byte2>96:
        byte2-=4
    elif byte2>64:
        byte2-=2
    elif byte2>37:
        byte2-=1
    byte3-=byte0
    while byte3<32:
        byte3+=88
    byte0+=3
    while byte0>87:
        byte0-=88
    byte3-=32
    byte4=data1[byte3]
    if byte2>125:
        byte2-=7
    elif byte2>96:
        byte2-=4
    elif byte2>64:
        byte2-=2
    elif byte2>37:
        byte2-=1
    byte4-=byte1
    while byte4<32:
        byte4+=88
    byte1+=1
    while byte1>87:
        byte1-=88
    if byte4>118:
        byte4+=7
    elif byte4>92:
        byte4+=4
    elif byte4>62:
        byte4+=2
    elif byte4>36:
        byte4+=1
    data4.append(byte4)
with open(name4,mode='wb')as file:
    file.write(bytes(data4))