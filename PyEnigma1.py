byte0=int(input())
name2=input()
name3=input()
data3=[]
with open('PyEnigma0',mode='rb')as file:
    data0=file.read()
with open('PyEnigma1',mode='rb')as file:
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
    byte2+=data0[byte0]
    while byte2>87:
        byte2-=88
    byte3=data1[byte2]
    byte0+=1
    while byte0>87:
        byte0-=88
    data3.append(byte3)
with open(name3,mode='wb')as file:
    file.write(bytes(data3))