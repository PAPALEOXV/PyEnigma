byte0=32
file1=open(input(),'rb')
data1=file1.read()
file1.close()
data2=[0]*89
for byte1 in data1:
    byte2=byte0
    if byte1>125:
        byte1-=6
    elif byte1>96:
        byte1-=3
    elif byte1>64:
        byte1-=1
    byte1-=32
    if byte2>119:
        byte2+=6
    elif byte2>93:
        byte2+=3
    elif byte2>63:
        byte2+=1
    data2[byte1]=byte2
    byte0+=1
    while byte0>120:
        byte0-=89
file2=open(input(),'wb')
file2.write(bytes(data2))
file2.close()