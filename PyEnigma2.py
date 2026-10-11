#Do not use in production
byte0=int(input())
name1=input()
name2=input()
data2=[]
with open('PyEnigma2',mode='rb')as file:
    data0=file.read()
with open(name1,mode='rb')as file:
    data1=file.read()
for byte1 in data1:
    if byte1>125:
        byte1-=5
    elif byte1>96:
        byte1-=2
    byte1-=32
    byte2=data0[byte1]
    if byte2>125:
        byte2-=5
    elif byte2>96:
        byte2-=2
    byte2-=byte0
    while byte2<32:
        byte2+=90
    byte0+=1
    while byte0>89:
        byte0-=90
    if byte2>120:
        byte2+=5
    elif byte2>94:
        byte2+=2
    data2.append(byte2)
print(len(data2))
with open(name2,mode='wb')as file:
    file.write(bytes(data2))