byte0=int(input())
byte1=int(input())
name0=input()
name1=input()
name2=input()
name4=input()
data4=[]
with open('PyEnigma'+name0,mode='rb')as file:
    data0=file.read()
with open('PyEnigma'+name1,mode='rb')as file:
    data1=file.read()
with open(name2,mode='rb')as file:
    data2=file.read()
for byte2 in data2:
    if byte2>125:
        byte2-=7
    elif byte2>96:
        byte2-=4
    elif byte2>63:
        byte2-=2
    elif byte2>36:
        byte2-=1
    byte2-=32
    byte2+=byte0
    while byte2>87:
        byte2-=88
    byte3=data0[byte2]
    byte0+=1
    while byte0>87:
        byte0-=88
    if byte3>125:
        byte3-=7
    elif byte3>96:
        byte3-=4
    elif byte3>63:
        byte3-=2
    elif byte3>36:
        byte3-=1
    byte3-=32
    byte3+=byte1
    while byte3>87:
        byte3-=88
    byte4=data1[byte3]
    byte1+=3
    while byte1>87:
        byte1-=88
    data4.append(byte4)
with open(name4,mode='wb')as file:
    file.write(bytes(data4))