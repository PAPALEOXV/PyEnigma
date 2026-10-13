#Do not use in production
byte0=int(input())
name1=input()
name2=input()
data2=[]
with open('PyEnigma1',mode='rb')as file:
    data0=file.read()
with open(name1,mode='rb')as file:
    data1=file.read()
for byte1 in data1:
    if byte1>125:
        byte1-=6
    elif byte1>96:
        byte1-=3
    elif byte1>63:
        byte1-=1
    byte1-=32
    byte1+=byte0
    while byte1>88:
        byte1-=89
    byte2=data0[byte1]
    byte0+=1
    while byte0>88:
        byte0-=89
    data2.append(byte2)
print(len(data2))
with open(name2,mode='wb')as file:
    file.write(bytes(data2))