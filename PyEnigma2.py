byte0=int(input())
file0=open('PyEnigma0','rb')
data0=file0.read()
file0.close()
file1=open('PyEnigma2','rb')
data1=file1.read()
file1.close()
file2=open(input(),'rb')
data2=file2.read()
file2.close()
data3=[]
for byte2 in data2:
    if byte2>125:
        byte2-=6
    elif byte2>96:
        byte2-=3
    elif byte2>64:
        byte2-=1
    byte2-=32
    byte3=data1[byte2]
    if byte3>125:
        byte3-=6
    elif byte3>96:
        byte3-=3
    elif byte3>64:
        byte3-=1
    byte3-=data0[byte0]
    while byte3<32:
        byte3+=89
    byte0+=1
    while byte0>88:
        byte0-=89
    if byte3>119:
        byte3+=6
    elif byte3>93:
        byte3+=3
    elif byte3>63:
        byte3+=1
    data3.append(byte3)
file3=open(input(),'wb')
file3.write(bytes(data3))
file3.close()